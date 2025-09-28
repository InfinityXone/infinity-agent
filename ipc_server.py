
import socket
import os

SOCKET_PATH = os.getenv("IPC_SOCKET_PATH", "/tmp/agent_one.sock")

if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(SOCKET_PATH)
server.listen()

print("🔌 IPC Server listening at", SOCKET_PATH)

while True:
    conn, _ = server.accept()
    data = conn.recv(1024).decode()
    print("💬 IPC Received:", data)
    if data == "status":
        conn.send(b"Agent online.")
    else:
        conn.send(b"Command received.")
    conn.close()
