import socket


class Server:
    def __init__(self, protocol, host, port):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, protocol)
        self.client_threads = []
        self.active = True

    def __del__(self):
        self.stop()

    def start(self):
        raise NotImplementedError("Subclasses must implement the start_server method.")

    def handle_connection(self, conn):
        raise NotImplementedError("Subclasses must implement the handle_connection method.")

    def stop(self):
        if self.active:
            self.socket.close()
            self.active = False
