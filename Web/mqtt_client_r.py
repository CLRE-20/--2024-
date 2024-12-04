import paho.mqtt.client as mqtt

# MQTT 伺服器設定
broker = "mqtt_broker.mcooest.us.kg"  # 替換為第一台伺服器的 IP 或主機名
port = 23419
topic = "mqtt/app"  # 替換為發送端使用的 topic
username = "web2"  # 使用者名稱
password = "web2"  # 密碼

# 當接收到訊息時的回調函數
def on_message(client, userdata, message):
    payload = message.payload.decode()  # 將接收到的訊息解碼
    print(f"接收到來自 {message.topic} 的訊息：{payload}")

# 當成功連接時的回調函數
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"成功連接到 MQTT Broker: {broker}")
        client.subscribe(topic)  # 訂閱指定的 topic
        print(f"已訂閱 topic: {topic}")
    else:
        print(f"無法連接到 MQTT Broker，錯誤碼: {rc}")

def start_mqtt_client():
    # 設置 MQTT 客戶端
    client = mqtt.Client()
    client.username_pw_set(username, password)

    # 設定回調函數
    client.on_connect = on_connect
    client.on_message = on_message

    # 連接到 MQTT 伺服器並開始非同步循環
    client.connect(broker, port, 60)
    client.loop_forever()  # 持續運行以保持連接

#paho-mqtt