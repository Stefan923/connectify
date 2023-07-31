from client.connection import Connection


class Client:
    def __init__(self, protocol, host, port):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.connections = []

    def __del__(self):
        self.close_all_connections()

    def open_connection(self):
        connection = Connection(self.protocol)
        self.connections.append(connection)
        return connection

    def close_all_connections(self):
        for connection in self.connections:
            connection.close()
        self.connections = []

    def send_data_without_receive(self, data):
        raise NotImplementedError("Subclasses must implement the send_data_without_receive method.")

    def send_data_and_receive_back(self, data):
        raise NotImplementedError("Subclasses must implement the send_data_and_receive_back method.")
