const aedes = require('aedes')();
const server = require('aedes-server-factory').createServer(aedes);
const port = 23419;

// 帳號密碼設置
const users = {
  'user1': 'password1',
  'user2': 'password2',
  'clre20':'123',
  'uptime':'uptime',
  'web1': 'web1',
  'web2': 'web2',
  'code':'server',
  'esp8266':'8266'
};

// 驗證客戶端的連接
aedes.authenticate = (client, username, password, callback) => {
  const validPassword = users[username];
  if (validPassword && password.toString() === validPassword) {
    console.log(`使用者已通過身份驗證: ${username}`);
    callback(null, true); // 驗證成功
  } else {
    console.log(`使用者身份驗證失敗: ${username}`);
    callback(null, false); // 驗證失敗
  }
};

// 監聽連接和斷開事件
aedes.on('client', (client) => {
  console.log(`客戶端已連接: ${client.id}`);
});

aedes.on('clientDisconnect', (client) => {
  console.log(`客戶端已斷開連接: ${client.id}`);
});

// 接收訊息並檢查 topic
aedes.on('publish', (packet, client) => {
  const topic = packet.topic;
  const message = packet.payload.toString();

  // 過濾掉 $SYS 系統主題
  if (topic.startsWith('$SYS/')) {
    return; // 直接跳過
  }

  // 檢查訊息是否為特定的 topic
  if (topic === 'my/specific/topic') {
    console.log(`收到訊息!!，主題:${topic}，訊息: ${message}`);
  } else {
    console.log(`未知訊息!!，主題:${topic}，訊息: ${message}`);
  }
});

// 啟動 MQTT Broker
server.listen(port, () => {
  console.log(`MQTT broker 正在連接埠上運行 ${port}`);
});

//aedes
//aedes-server-factory
