#include <WiFi.h>
#include <PubSubClient.h>
#include <ESP32Servo.h> // 伺服馬達

// WiFi 和 MQTT 配置
const char* ssid = "mc";//Doludo
const char* password = "12345678";//077108100
const char* mqttServer = "mqtt_broker.mcooest.us.kg";
const int mqttPort = 23419;
const char* mqttUser = "esp8266";
const char* mqttPassword = "8266";

// MQTT 客戶端
WiFiClient espClient;
PubSubClient client(espClient);

// 創建 Servo 實例
Servo myservo;
int servoPin=14;

void setup() {
  // 初始化序列埠
  Serial.begin(115200);
  delay(10);

  // 連接WiFi
  Serial.print("正在連線 WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("成功連上!");

  // 設置MQTT伺服器
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  // 連接MQTT伺服器
  connectToMQTT();
  // 初始化伺服馬達，假設連接在 D4 引腳
  myservo.attach(servoPin);  // 設置舵機控制腳位
  myservo.write(120); // 初始化伺服馬達為 30 度
  //繼電器
  pinMode(12,OUTPUT);
  digitalWrite(12,HIGH);
}

void connectToMQTT() {
  while (!client.connected()) {
    Serial.print("正在連線 MQTT...");
    if (client.connect("ESP8266Client", mqttUser, mqttPassword)) {
      Serial.println("成功連上!");
      // 訂閱 /mqtt/app 主題
      client.subscribe("mqtt/app");
    } else {
      Serial.print("錯誤碼, rc=");
      Serial.print(client.state());
      Serial.println(" 5 秒後重來");
      delay(5000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  // 將接收到的 payload 轉成字串
  String receivedMessage = "";
  for (int i = 0; i < length; i++) {
    receivedMessage += (char)payload[i];
  }
  // 如果主題是 /mqtt/app，打印特別提示
  if (String(topic) == "mqtt/app" && receivedMessage == "power") {
    Serial.print("通過認證");
    Serial.print("訊息：");
    Serial.print("[");
    Serial.print(receivedMessage);
    Serial.print("]，來自[");
    Serial.print(topic);
    Serial.println("]路由");
    digitalWrite(12,HIGH);
  }
  else if (String(topic) == "mqtt/app" && receivedMessage == "Door") {
    myservo.write(120); // 初始化伺服馬達為 30 度
    Serial.print("通過認證");
    Serial.print("訊息：");
    Serial.print("[");
    Serial.print(receivedMessage);
    Serial.print("]，來自[");
    Serial.print(topic);
    Serial.println("]路由");
  }
  else if (String(topic) == "mqtt/app" && receivedMessage == "earthquake") {
    myservo.write(50); // 初始化伺服馬達為 120 度
    Serial.print("通過認證");
    Serial.print("訊息：");
    Serial.print("[");
    Serial.print(receivedMessage);
    Serial.print("]，來自[");
    Serial.print(topic);
    Serial.println("]路由");
    digitalWrite(12,LOW);
  }
  else {
    Serial.print("認證失敗!!");
    Serial.print("訊息：");
    Serial.print("[");
    Serial.print(receivedMessage);
    Serial.print("]，來自[");
    Serial.print(topic);
    Serial.println("]路由");
  }
}

void loop() {
  // 保持MQTT連接
  if (!client.connected()) {
    connectToMQTT();
  }
  client.loop();

  // 發送測試訊息至 /mqtt/esp8266
  //client.publish("/mqtt/esp8266", "Hello from ESP8266");
  //delay(10000); // 每10秒發送一次
}
//https://dl.espressif.com/dl/package_esp32_index.json
