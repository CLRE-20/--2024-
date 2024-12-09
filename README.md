# 2024 地震斷電系統 - 專題製作

本專題旨在開發一套地震斷電系統，利用現代物聯網技術，實現快速反應與智慧化控制。本系統由手機應用程式、控制面板、ESP8266 開發板及 MQTT 通訊協議共同組成，並搭配 SQLite 資料庫進行數據管理，實現了高效、穩定的地震警報與自動斷電功能。此外，為提升系統安全性，MQTT 通訊使用帳號和密碼進行認證，確保數據傳輸的安全。

---

## 目錄

1. [手機 App](#手機-app)  
2. [控制面板](#控制面板)  
3. [ESP8266 開發板](#esp8266-開發板)  
4. [MQTT 通訊](#mqtt-通訊)  
5. [資料庫管理](#資料庫管理)  

---

## 手機 App

**手機應用程式負責提供用戶操作介面，整合系統功能並實現與機器互動。**

### 技術細節
1. 使用 **Android Studio** 開發，提供高效能且易於維護的 Android 應用程式。  
   [下載 Android Studio](https://developer.android.com/studio?hl=zh-tw)  
2. 透過 **WebView** 嵌入控制面板，使得用戶能在 App 中直接操作系統功能。
3. 支援返回鍵與網站的交互操作，提升用戶體驗與流暢性。

---

## 控制面板

**控制面板為本系統的核心邏輯處理模組，負責數據管理、前後端交互及操作指令發送。**

### 運行環境
- **開發語言**：Python  
- **框架與工具**：Flask、Flask-Login、Flask-SQLAlchemy、Paho-MQTT。

### 功能特點
- **模擬地震**：測試系統對地震信號的反應。
- **復電功能**：地震結束後，可執行安全檢查並恢復電力。
- **關門功能**：模擬智能門鎖，地震期間自動關閉。
- **用戶管理**：支持註冊、登入、密碼重置，並需綁定產品編號。
- **數據交互**：與 MQTT 通訊實現數據發布與接收。
- **安全性**：通過 MQTT 帳號密碼驗證，確保數據傳輸安全。
- **實時監控**：地震警報與電力狀態。

![圖](https://raw.githubusercontent.com/clre20/Earthquake-power-system-2024-Topics/refs/heads/app.py/panel.jpg)
---

## ESP8266 開發板

**ESP8266 是本系統的硬體核心，負責感測器數據的收集與通訊模組的控制。**

### 功能
1. **地震數據收集**：與感測器聯動，實時傳輸數據。
2. **指令執行**：接收控制面板指令，如斷電、復電操作。
3. **數據傳輸**：通過 WiFi 與 MQTT 伺服器進行通信。

### 技術實現
- 使用 **Arduino IDE** 進行程式設計。
- 配置 WiFi 功能，實現高效的無線數據傳輸。
- 支援 **OTA（Over-the-Air）更新**，便於系統升級與維護。

---

## MQTT 通訊

**MQTT 是本系統的通訊骨幹，負責數據的高效傳遞與消息發布，並採用帳號密碼驗證以增強安全性。**

### MQTT 伺服器
1. **運行環境**：使用 **JavaScript** 建立 MQTT 伺服器，選用輕量級 Broker（如 Mosquitto 或 EMQX）。  
2. **功能**：
   - 管理消息的接收與分發。
   - 支援帳號和密碼認證，限制未授權設備訪問。

### MQTT 客戶端
1. **運行環境**：使用 Python 開發，與控制面板結合運作。
2. **功能**：
   - 接收地震感測器數據，並發布到伺服器。
   - 確保 ESP8266 與控制面板之間的實時通信。

![圖](https://raw.githubusercontent.com/clre20/Earthquake-power-system-2024-Topics/refs/heads/app.py/mqtt.jpg)
---

## 資料庫管理

**本系統使用 SQLite 作為輕量化資料庫，負責存儲用戶數據、警報記錄及系統設置。**

### 技術特點
1. **輕量簡便**：SQLite 是嵌入式資料庫，適合小型應用，無需額外伺服器支援。
2. **整合性強**：與 Flask-SQLAlchemy 無縫結合，方便數據操作。
3. **資料結構**：
   - **用戶表**：儲存用戶帳號、密碼（加密存儲）、產品編號等信息。
   - **警報記錄表**：儲存地震時間、強度、執行的操作（斷電或復電）。
   - **系統設置表**：記錄 MQTT 配置（伺服器地址、帳號密碼等）。

---

## 安全設計

1. **MQTT 帳號密碼驗證**：限制未授權設備訪問，防止數據攔截與非法操作。
2. **密碼加密存儲**：用戶密碼經加密（如 SHA-256 或 bcrypt）存儲，防範數據洩露。
3. **SSL/TLS 加密**：可選擇在 MQTT 通訊中啟用 SSL/TLS，確保數據傳輸安全。

---

## 系統架構圖

```plaintext
[ESP8266 開發板] <--> [MQTT 伺服器] <--> [控制面板] <--> [手機 App]
                                |
                          [SQLite 資料庫]
```
---

## 總結

本系統結合物聯網技術與輕量化開發工具，實現了智慧化地震斷電系統的設計，具備以下特點：
1. 整合軟硬體，實現數據的實時交互。
2. 安全設計到位，防止未授權訪問與數據洩露。
3. 支援用戶友好操作界面，提供多樣化功能如模擬地震、智能復電。

此系統適用於地震頻發地區，能有效提升用戶的安全感與便捷性。

