import struct

from server.server import Server

import threading


class TCPServer(Server):
    def __init__(self, protocol, host, port, buffer_size=4096):
        super().__init__(protocol, host, port)
        self.__buffer_size = buffer_size

    def start(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen()

            while True:
                conn, addr = self.socket.accept()
                client_thread = threading.Thread(target=self.handle_connection, args=(conn,))
                client_thread.start()

        except Exception as e:
            print(f"Error occurred in the server: {e}")
        finally:
            self.socket.close()

    def handle_connection(self, conn):
        try:
            with conn:
                while self.active:
                    received_data_length = self.__recv_all(conn, 4)
                    if len(received_data_length) == 0:
                        return

                    data_length = struct.unpack('!i', received_data_length)[0]
                    received_data = self.__recv_all(conn, data_length).decode('utf-8')
                    if len(received_data) == 0:
                        return

                    conn.send(struct.pack('!i', data_length))
                    conn.sendall(received_data.encode('utf-8'))
        except Exception as e:
            print(f"Error occurred in handling connection: {e}\n")

    def __recv_all(self, conn, size):
        received_data = b""
        while len(received_data) < size:
            remaining_bytes = size - len(received_data)
            chunk = conn.recv(min(remaining_bytes, self.__buffer_size))
            if not chunk:
                break
            received_data += chunk
        return received_data
