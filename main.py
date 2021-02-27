from flask import Flask, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 18
GPIO.setup(FAN_PIN, GPIO.OUT)


@app.route('/on')
def turn_on():
    try:
        GPIO.output(FAN_PIN, True)
    except Exception:
        return jsonify({"status": "error"})
    else:
        return jsonify({"status": "ok"})


@app.route('/off')
def turn_of():
    try:
        GPIO.output(FAN_PIN, False)
    except Exception:
        return jsonify({"status": "error"})
    else:
        return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run("0.0.0.0", 50000)
