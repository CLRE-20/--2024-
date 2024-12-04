import json

data_power = {}
data_door = {}
data_earthquake = {}

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
    run_earthquake()

def earthquake_finish():
    open_json_earthquake_r()
    data_earthquake["earthquake"] = "無地震發生"  # 更新 earthquake 的值
    open_json_earthquake_w()

#run()