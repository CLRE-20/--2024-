import json
data = {}

def open_json_r():  
    global data  # 使用全局變數
    # 讀取json
    with open("data.json", mode="r", encoding='utf-8') as file:
        data = json.load(file)
        return data

def open_json_w():  
    global data  # 使用全局變數
    # 讀取json
    with open("data.json", mode="w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    # 加上 indent=4 參數以進行格式化
    print(data)

def run():
    open_json_r()
    data["door"]="關"
    open_json_w()

def implement():
    open_json_r()
    data["door"] = "動作執行中!"  # 更新 power 的值
    open_json_w()
#run()