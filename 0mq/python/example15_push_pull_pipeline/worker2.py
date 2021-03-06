import zmq
from zmq.decorators import context, socket
from os import getpid


IN_PORT = 5557
OUT_PORT = 5558


@context()
@socket(zmq.PULL)
@socket(zmq.PUSH)
def start_worker(context, in_socket, out_socket):
    """Spuštění workera."""

    address = "tcp://localhost:{port}".format(port=IN_PORT)
    in_socket.connect(address)
    print("Connected to {a}".format(a=address))

    address = "tcp://localhost:{port}".format(port=OUT_PORT)
    out_socket.connect(address)
    print("And to {a}".format(a=address))

    print("Waiting for message from worker #1...")
    pid = getpid()

    while True:
        message = in_socket.recv_string()
        out_message = "Message from {pid}: '{m}'".format(pid=pid, m=message)
        print(out_message)
        out_socket.send_string(out_message)


start_worker()
