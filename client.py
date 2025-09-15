import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def connect_to_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            data = s.recv(1024)
            print('Received from server:', data.decode())
        except ConnectionRefusedError:
            print("Failed to connect to server. Is the server running?")
        except OSError as e:
            print(f"Client error: {e}")

if __name__ == "__main__":
    connect_to_server()