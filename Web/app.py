from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import random
import string
import json
import mqtt_client_s_earthquake #mqtt發送端-地震模擬
import mqtt_client_s_power #mqtt發送端-復電
import mqtt_client_s_door #mqtt發送端-關門
import mqtt_client_r #mqtt接收端
import power #電源
import door #門
import earthquake #地震
import login_utils #登入
import threading
import time

app = Flask(__name__)

app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    product_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # 使用 ID 來查詢，而不是 email

#讀取 data.json -面板刷新
def load_json_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
# 讀取 products.json 資料
def load_json_products():
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def index():
    return redirect(url_for('panel'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = 'remember' in request.form

        user = User.query.filter_by(email=email).first()  # 假設你用 SQLAlchemy
        if user and user.password == password:  # 比對密碼是否正確
            login_user(user, remember=remember)
            next_page = request.args.get('next')  # 檢查是否有 "next" 參數
            if next_page:  # 如果有 "next" 參數，重定向到原來頁面
                return redirect(next_page)
            else:  # 否則導向預設頁面
                # 儲存登入資料到 data.json
                login_utils.save_login_data_to_json(user.email, user.product_id)  # 這裡調用 login.py 中的函式
                login_utils.save_login_data_to_json(user.email, user.product_id)  # 這裡調用 login.py 中的函式

                return redirect(url_for('panel'))  # panel 頁面
        else:
            flash('無效的憑證')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        product_id = request.form['product_id']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        with open('products.json', 'r') as f:
            products = json.load(f)
        
        if existing_user:
            flash('電子郵件已存在')
        elif product_id not in products or products[product_id] is not None:
            flash('產品編號無效或已註冊')
        else:
            new_user = User(email=email, product_id=product_id, password=password)
            db.session.add(new_user)
            db.session.commit()
            products[product_id] = email
            with open('products.json', 'w') as f:
                json.dump(products, f, indent=4)  # Pretty print JSON with indentation
            flash('註冊成功，請登入')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        product_id = request.form['product_id']
        user = User.query.filter_by(email=email, product_id=product_id).first()
        if user:
            # 生成簡單的驗證碼
            verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            session['verification_code'] = verification_code
            session['reset_email'] = email
            flash(f'您的驗證碼是：{verification_code}')  # 顯示驗證碼，僅用於演示目的
            return redirect(url_for('verify_code'))
        else:
            flash('找不到電子郵件或產品編號')
    return render_template('forgot_password.html')

@app.route('/verify_code', methods=['GET', 'POST'])
def verify_code():
    if request.method == 'POST':
        code = request.form['code']
        if code == session.get('verification_code'):
            return redirect(url_for('reset_password'))
        else:
            flash('無效的驗證碼')
    return render_template('verify_code.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    email = session.get('reset_email')
    if not email:
        flash('會話過期或無效')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        new_password = request.form['password']
        user = User.query.filter_by(email=email).first()
        user.password = new_password
        db.session.commit()
        flash('您的密碼已更新')
        return redirect(url_for('login'))
    return render_template('reset_password.html')

#------------------------------面板------------------------------

@app.route('/panel')
@login_required
def panel():
    print(f"Session data: {session}")
    print(f"Current user: {current_user.is_authenticated}")
    return render_template('panel.html')

@app.route('/powerMQTT')
def powerMQTT():
    power.implement() # 顯示運作
    mqtt_client_s_power.run_test()  # mqtt
    power.run()  # 更新狀態
    return "復電！"

@app.route('/doorMQTT')
def DoorMQTT():
    door.implement() # 顯示運作
    mqtt_client_s_door.run_test()  # mqtt
    door.run()  # 更新狀態
    return "關門！"

@app.route('/earthquakeMQTT')
def earthquakeMQTT():
    mqtt_client_s_earthquake.run_test()  # mqtt
    earthquake.run()  # 更新狀態
    time.sleep(30)
    earthquake.earthquake_finish()
    return "地震模擬！"

@app.route('/data')
def data():
    #products = load_json_products()  # 獲取登入資料
    data = load_json_data()          # 獲取面板資料

    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 確保資料庫結構建立

    # 創建和啟動 MQTT 客戶端的執行緒
    mqtt_thread = threading.Thread(target=mqtt_client_r.start_mqtt_client)
    mqtt_thread.start()
    
    # 啟動 Flask 應用
    app.run(debug=True, host='0.0.0.0', port=23028)
