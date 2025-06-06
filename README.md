
---

````markdown
# 🌦️ RaspiClimateMonitor

**RaspiClimateMonitor** is a simple yet powerful IoT project that uses a Raspberry Pi and DHT11 sensor to monitor temperature and humidity in real-time. It sends the data to Firebase Realtime Database using Python and displays it on a live, responsive web dashboard built with HTML, CSS, and JavaScript.

---

## 📸 Preview

> Real-time climate data displayed on a Firebase-powered web dashboard.

![Demo Screenshot](screenshot.png) <!-- Optional: Add your dashboard screenshot here -->

---

## 🚀 Key Features

- 🌡️ Measures temperature and humidity using the DHT11 sensor
- 🔄 Syncs sensor data to Firebase using Python
- ☁️ Stores readings in Firebase Realtime Database
- 🖥️ Displays live updates on a web dashboard
- 📱 Mobile-friendly UI built with HTML, CSS, and JavaScript

---

## 🛠️ Tech Stack

| Layer         | Technologies Used                           |
|---------------|---------------------------------------------|
| **Hardware**  | Raspberry Pi 4, DHT11 Temperature Sensor     |
| **Backend**   | Python, Firebase Admin SDK                   |
| **Database**  | Firebase Realtime Database                   |
| **Frontend**  | HTML, CSS, JavaScript, Firebase JS SDK       |

---

## 🧰 Hardware Setup

**Connect your DHT11 sensor to the Raspberry Pi GPIO as follows:**

| DHT11 Pin | Raspberry Pi Pin     |
|-----------|-----------------------|
| VCC       | 3.3V (Pin 1)          |
| GND       | GND (Pin 6)           |
| DATA      | GPIO17 (Pin 11)       |

---

## ⚙️ Getting Started

### 🔌 Raspberry Pi Setup

1. Wire the DHT11 sensor as shown above.
2. Install required libraries:
   ```bash
   pip install adafruit-circuitpython-dht firebase-admin
   sudo apt install libgpiod2
````

3. Run the script:

   ```bash
   sudo python3 main.py
   ```

### ☁️ Firebase Configuration

1. Visit [Firebase Console](https://console.firebase.google.com/) and create a new project.
2. Enable **Realtime Database** and set it to test mode.
3. Navigate to **Project Settings → Service Accounts**, then generate a new private key.
4. Download and save it as `serviceAccountKey.json` in your project folder.

### 🖥️ Web Dashboard Setup

1. In Firebase, register a new Web App.
2. Copy the Firebase configuration snippet and paste it into `script.js`.
3. Open `index.html` in your browser to see the real-time climate data.

---

## 🔐 Firebase Database Rules (for testing)

```json
{
  "rules": {
    ".read": "now < 1751740200000",
    ".write": "now < 1751740200000"
  }
}
```

---

## 💡 Applications

* Smart Home environment monitoring
* Weather station prototypes
* IoT learning projects
* Real-time dashboards for classrooms or labs

---

## 📜 License

This project is licensed under the MIT License. You’re free to use, share, and modify it.

---

## 🤝 Contributing

Got an idea or improvement? Pull requests are welcome! For major changes, please open an issue first.

---
