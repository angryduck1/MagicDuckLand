import socket
from DuckLandServer.Network.Connection.Connection import Connection

class TcpNetwork:
    def __init__(self, address) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        print("Welcome to DuckLand! ")

        print(f"Server is listening at {address}")

        while True:
            self.server.listen()
            connection, addr = self.server.accept()
            print(f"New connection from {addr[0]}:{addr[1]}")
            
            Connection(connection, addr).start()