import time
import board
import adafruit_dht
import firebase_admin
from firebase_admin import credentials, db

# Initialize DHT11 sensor on GPIO17
dht_sensor = adafruit_dht.DHT11(board.D17)

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")  # your Firebase service account JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pitempmonitor-default-rtdb.firebaseio.com'
})

try:
    while True:
        temperature_c = dht_sensor.temperature
        humidity = dht_sensor.humidity

        if temperature_c is not None and humidity is not None:
            print(f"Temperature: {temperature_c} °C, Humidity: {humidity} %")

            # Write both values to Firebase
            db.reference("sensorData").set({
                "temperature": temperature_c,
                "humidity": humidity
            })
        else:
            print("Failed to get reading.")

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped.")
except Exception as e:
    print(f"Error: {e}")
