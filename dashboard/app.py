from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

LOG_FILE = "logs/alerts.log"


@app.route("/")
def index():
    return render_template("index.html")


def stream_logs():
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            log = json.loads(line)
            socketio.emit("new_log", log)


@socketio.on("connect")
def handle_connect():
    print("Client connected")


if __name__ == "__main__":
    print("🚀 Starting Dashboard Server...")
    socketio.start_background_task(stream_logs)
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
