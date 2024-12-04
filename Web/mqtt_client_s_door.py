import paho.mqtt.client as mqtt
import os
import json
import time

# MQTT 伺服器設定
broker = "mqtt_broker.mcooest.us.kg"
port = 23419
topic = "mqtt/app"
username = "web1"  # 如果需要使用者名稱和密碼，請修改
password = "web1"  # 如果需要使用者名稱和密碼，請修改

# 建立 MQTT 客戶端
client = mqtt.Client()

# 設定使用者名稱和密碼（如果需要）
client.username_pw_set(username, password)

# 當客戶端連接成功時的回調函數
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"成功連接到 MQTT Broker: {broker}")
    else:
        print(f"無法連接到 MQTT Broker，錯誤碼: {rc}")

# 當消息發佈成功時的回調函數
def on_publish(client, userdata, mid):
    print(f"發佈成功，消息ID: {mid}")

# 設定回調函數
client.on_connect = on_connect
client.on_publish = on_publish

# 連接到 MQTT Broker，失敗時自動重試，無限次
def connect_broker():
    while True:
        try:
            print(f"正在連接到 {broker}...")
            client.connect(broker, port, 60)
            client.loop_start()  # 啟動非同步循環，讓客戶端持續處理事件
            return  # 連接成功後跳出循環
        except Exception as e:
            print(f"無法連接到 MQTT Broker: {e}")
            print("5秒後重新連接...")
            time.sleep(5)  # 等待 5 秒後重試

# 測試發佈數值，添加重試機制
def publish_value():

    json_path = "mqtt_client.json"
    # 確認檔案是否存在
    if not os.path.exists(json_path):
        print(f"檔案 {json_path} 不存在，請確認路徑和名稱是否正確")
        return
    
    # 讀取json
    with open("mqtt_client.json", mode="r") as file:
        data = json.load(file)
    print("Door", data["Door"])  # 指定

    payload = f'{data["Door"]}'  # 修改這行使用單引號來避免引號衝突
    attempt = 0  # 重試歸零

    while attempt < 3:  # 最多重試 3 次
        try:
            if client.is_connected():  # 確認連線狀態
                result = client.publish(topic, payload, qos=1)  # 設定 QoS 等級為 1
                status = result.rc
                if status == 0:
                    print(f"已成功發佈: {payload}")
                    break  # 成功發佈則退出重試
                else:
                    print(f"發佈失敗，狀態碼: {status}")
            else:
                print("連線已斷開，重新連接中...")
                connect_broker()  # 重新連接
        except Exception as e:
            print(f"發佈消息時出現錯誤: {e}")

        attempt += 1
        print("5秒後重試發佈...")
        time.sleep(5)

# 執行測試，無限次重試直到成功連接並發佈消息
def run_test():
    connect_broker()  # 先進行初始連接
    a= 1
    while a == 1:
        # 連接成功後進行發佈測試
        publish_value()
        #time.sleep(5)  # 每 5 秒發佈一次
        a = 0

#if __name__ == "__main__":
#    run_test()

#paho-mqtt