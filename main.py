from flask import Flask, jsonify
import RPi.GPIO as GPIO
import os
import re

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 18
GPIO.setup(FAN_PIN, GPIO.OUT)


@app.route('/on')
def turn_on():
    try:
        channel_state = GPIO.input(FAN_PIN)
        if channel_state:
            return jsonify({"status": "ok"})
        GPIO.output(FAN_PIN, True)
        return jsonify({"status": "ok"})
    except Exception:
        return jsonify({"status": "error"})

@app.route('/off')
def turn_of():
    try:
        GPIO.output(FAN_PIN, False)
        channel_state = GPIO.input(FAN_PIN)
        if not channel_state:
            return jsonify({"status": "ok"})
        return jsonify({"status": "ok"})
    except Exception:
        return jsonify({"status": "error"})

@app.route('/')
def measure_temp():
    current_state = 'on' if GPIO.input(FAN_PIN) else 'off'
    try:
        raw = os.popen('vcgencmd measure_temp').readline()
        m = re.match("temp=(\d+\.?\d*)'C", raw)
        if not m:
            raise ValueError("Unexpected temperature string:" + raw)
        current_temp = float(m.group(1))
    except ValueError:
        current_temp = None

    return jsonify({"current_temp": current_temp, "current_fan_state": current_state})


if __name__ == "__main__":
	app.run("0.0.0.0", 50000)
