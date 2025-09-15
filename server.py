import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            print(f"Server listening on {HOST}:{PORT}...")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                message = "Hello from server!"
                conn.sendall(message.encode())
        except OSError as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()