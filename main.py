import socket
import threading

from client.tcp_client import TCPClient
from server.tcp_server import TCPServer

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 20001

    server = TCPServer(socket.SOCK_STREAM, server_ip, server_port)
    client = TCPClient(socket.SOCK_STREAM, server_ip, server_port)

    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    data_to_send = "Hello, Server!"

    result1 = client.send_data_without_receive(data_to_send)
    print("Sent Data:", result1.sent_data)
    print("Total Time:", result1.total_time)

    result2 = client.send_data_and_receive_back(data_to_send)
    print("Sent Data:", result2.sent_data)
    print("Received Data:", result2.received_data)
    print("Total Time:", result2.total_time)

    server_thread.join()
