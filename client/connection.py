import socket


class Connection:
    def __init__(self, protocol):
        self.protocol = protocol
        self.socket = socket.socket(socket.AF_INET, protocol)
        self.connected = False

    def __del__(self):
        self.close()

    def start(self, host, port):
        try:
            self.socket.connect((host, port))
            self.connected = True
        except Exception as e:
            print(f"Error occurred during connection: {e}")

    def close(self):
        if self.connected:
            self.socket.close()
            self.connected = False
