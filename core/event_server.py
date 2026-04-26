from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*", async_mode="threading")


def emit_log(data):
    socketio.emit("new_log", data)
