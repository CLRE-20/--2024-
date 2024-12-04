import json

def save_login_data_to_json(email, product_id):
    # 嘗試讀取現有的 data.json 文件
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # 更新資料
    data['email'] = email
    data['product_id'] = product_id

    # 寫入更新後的資料
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Login info saved: {data}")
