
---

```markdown
# 🌦️ RaspiClimateMonitor

RaspiClimateMonitor is an end-to-end IoT project built with a Raspberry Pi and a DHT11 sensor to monitor temperature and humidity in real-time. The data is pushed to Firebase Realtime Database using Python and displayed on a responsive web dashboard using HTML, CSS, and JavaScript.

---

## 📸 Preview

> Live data on Firebase + Web Dashboard

![Demo Screenshot](screenshot.png) <!-- Optional: Add your dashboard screenshot -->

---

## 🚀 Features

- 🌡️ Real-time Temperature and Humidity sensing via DHT11
- 📡 Raspberry Pi + Python-based Firebase sync
- ☁️ Firebase Realtime Database for cloud data storage
- 🌐 Web-based Dashboard using Firebase JS SDK
- 📊 Clean and responsive UI (HTML, CSS, JavaScript)

---

## 🛠️ Tech Stack

| Layer         | Technology                           |
|---------------|---------------------------------------|
| **Hardware**  | Raspberry Pi 4, DHT11 Sensor          |
| **Backend**   | Python, Firebase Admin SDK            |
| **Database**  | Firebase Realtime Database            |
| **Frontend**  | HTML, CSS, JavaScript, Firebase JS SDK|

---

## 🧰 Hardware Setup

**Connections (DHT11 to Raspberry Pi GPIO):**

| DHT11 Pin | Connects To        |
|-----------|--------------------|
| VCC       | 3.3V (Pin 1)        |
| GND       | GND (Pin 6)         |
| DATA      | GPIO17 (Pin 11)     |

---

## ⚙️ Setup Instructions

### 🔌 Raspberry Pi + Sensor

1. Connect the DHT11 sensor to Raspberry Pi (see above wiring).
2. Install dependencies:
   ```bash
   pip install adafruit-circuitpython-dht firebase-admin
   sudo apt install libgpiod2


3. Run the Python script:

   ```bash
   sudo python3 main.py
   ```

### 🌐 Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project (e.g. `RaspiClimateMonitor`)
3. Enable Realtime Database (test mode)
4. Go to Project Settings → Service Accounts → Generate new private key
5. Save it as `serviceAccountKey.json` in your project directory

### 🖥️ Web Dashboard

1. Create a Firebase Web App (under Project Settings)
2. Copy the Firebase Config into `script.js`
3. Open `index.html` in your browser to view real-time data

---

## 📌 Firebase Rules (optional test mode)

```json
{
  "rules": {
    ".read": "now < 1751740200000",
    ".write": "now < 1751740200000"
  }
}
```

---

## 💡 Use Cases

* Smart Home Climate Monitoring
* IoT Learning & Prototyping
* Remote Weather Station
* Real-Time Environmental Dashboards

---

## 📜 License

MIT License – feel free to use and modify.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---
````
 
