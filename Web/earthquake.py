import json
import time
import random

data_power = {}
data_door = {}
data_earthquake = {}
data_state = {}
data_level = {}
data_area = {}

# 地震等級列表
level = ['4級', '5弱', '5強', '6弱', '6強', '7級']

# 台灣地區列表
area = [
    '臺北市', '新北市', '基隆市', '桃園市', '新竹市', '新竹縣',
    '苗栗縣', '臺中市', '彰化縣', '南投縣', '雲林縣', '嘉義市',
    '嘉義縣', '臺南市', '高雄市', '屏東縣', '宜蘭縣', '花蓮縣',
    '臺東縣', '澎湖縣', '金門縣', '連江縣'
]
# 從地震等級列表中隨機選擇一個地震等級
random_level = random.choice(level)
# 從台灣地區列表中隨機選擇一個地區
random_area = random.choice(area)

def open_json_power_r():  
    global data_power  # 使用全局變數
    with open("data.json", mode="r", encoding='utf-8') as file:
        data_power = json.load(file)
    return data_power

def open_json_power_w():  
    global data_power  # 使用全局變數
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data_power, file, indent=4)
    print(data_power)

def open_json_door_r():  
    global data_door  # 使用全局變數
    with open("data.json", mode="r", encoding='utf-8') as file:
        data_door = json.load(file)
    return data_door

def open_json_door_w():  
    global data_door  # 使用全局變數
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data_door, file, indent=4)
    print(data_door)

def open_json_earthquake_r():  
    global data_earthquake  # 使用全局變數
    with open("data.json", mode="r", encoding='utf-8') as file:
        data_earthquake = json.load(file)
    return data_earthquake

def open_json_earthquake_w():  
    global data_earthquake  # 使用全局變數
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data_earthquake, file, indent=4)
    print(data_earthquake)

def open_json_state_r():  
    global data_state  # 使用全局變數
    with open("data.json", mode="r", encoding='utf-8') as file:
        data_state = json.load(file)
    return data_state

def open_json_state_w():  
    global data_state  # 使用全局變數
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data_state, file, indent=4)
    print(data_state)

def open_json_level_r():  
    global data_level  # 使用全局變數
    with open("data.json", mode="r", encoding='utf-8') as file:
        data_level = json.load(file)
    return data_level

def open_json_level_w():  
    global data_level  # 使用全局變數
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data_level, file, indent=4)
    print(data_level)

def open_json_area_r():  
    global data_area  # 使用全局變數
    with open("data.json", mode="r", encoding='utf-8') as file:
        data_area = json.load(file)
    return data_area

def open_json_area_w():  
    global data_area  # 使用全局變數
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data_area, file, indent=4)
    print(data_area)

def run_power():
    open_json_power_r()
    data_power["power"] = "關"  # 更新 power 的值
    open_json_power_w()

def run_door():
    open_json_door_r()
    data_door["door"] = "開"  # 更新 door 的值
    open_json_door_w()

def run_earthquake():
    open_json_earthquake_r()
    data_earthquake["earthquake"] = "地震發生，請注意家中狀況!!"  # 更新 earthquake 的值
    open_json_earthquake_w()

def run():
    run_power()
    run_door()

def earthquake_finish():
    open_json_earthquake_r()
    data_earthquake["earthquake"] = " "  # 更新 earthquake 的值
    data_earthquake["level"] = " "
    data_earthquake["area"] = " "
    open_json_earthquake_w()

def earthquake_state_mqtt(): # 運行狀態
    open_json_state_r()
    data_state["state"] = "透過MQTT發送請求..."
    open_json_state_w()

def earthquake_state_power_door_1(): # 運行狀態
    open_json_state_r()
    data_state["state"] = "動作執行，並更新狀態..."
    open_json_state_w()
    time.sleep(2)

def earthquake_state_power_door_2(): # 運行狀態
    open_json_state_r()
    data_state["state"] = "狀態更新完畢"
    open_json_state_w()

def earthquake_sleep():
    open_json_state_r()
    data_state["state"] = " " # 更新 state 的值
    open_json_state_w()

def earthquake_level():
    open_json_level_r()
    data_level["level"] = random_level # 更新 state 的值
    open_json_level_w()

def earthquake_area():
    open_json_area_r()
    data_area["area"] = random_area # 更新 state 的值
    open_json_area_w()

#run()