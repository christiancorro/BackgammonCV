from datetime import datetime
import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5555")

while True:
    start = time.time()

    # _, frame = capture.read()
    data = {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}

    socket.send_json(data)

    end = time.time()
