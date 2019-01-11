import zmq
import sys
import time


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    return socket


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send(message)


def start_client():
    socket = connect(5556, zmq.PAIR)
    print("Waiting for messages...")
    while True:
        message = socket.recv_string()
        print(message)
        socket.send_string("Acknowledge... " + message)


start_client()