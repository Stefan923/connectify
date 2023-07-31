import struct

from server.server import Server

import threading


class TCPServer(Server):
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
                    received_data_length = conn.recv(4)
                    data_length = struct.unpack('!i', received_data_length)[0]
                    received_data = conn.recv(data_length).decode()

                    conn.send(struct.pack('!i', data_length))
                    conn.sendall(received_data.encode())

        except Exception as e:
            print(f"Error occurred in handling connection: {e}")
