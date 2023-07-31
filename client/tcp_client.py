import struct

from client.client import Client
from common.connection_result import ConnectionResult

import time


class TCPClient(Client):
    def send_data_without_receive(self, data):
        sent_data = None
        start_time = time.time()

        try:
            connection = self.open_connection()
            connection.start(self.host, self.port)

            data_length = len(data)
            connection.socket.send(struct.pack('!i', data_length))

            connection.socket.sendall(data.encode())
            sent_data = data
        except Exception as e:
            print(f"Error occurred during sending data: {e}")
        finally:
            self.close_all_connections()

        total_time = time.time() - start_time
        return ConnectionResult(sent_data, None, total_time)

    def send_data_and_receive_back(self, data):
        sent_data = None
        received_data = None
        start_time = time.time()

        try:
            connection = self.open_connection()
            connection.start(self.host, self.port)

            data_length = len(data)
            connection.socket.send(struct.pack('!i', data_length))

            connection.socket.sendall(data.encode())
            sent_data = data

            received_data_length = connection.socket.recv(4)
            data_length = struct.unpack('!i', received_data_length)[0]
            received_data = connection.socket.recv(data_length).decode()
        except Exception as e:
            print(f"Error occurred during sending/receiving data: {e}")
        finally:
            self.close_all_connections()

        total_time = time.time() - start_time
        return ConnectionResult(sent_data, received_data, total_time)
