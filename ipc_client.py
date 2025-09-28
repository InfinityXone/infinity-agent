
import socket
import sys
import os

SOCKET_PATH = os.getenv("IPC_SOCKET_PATH", "/tmp/agent_one.sock")
msg = " ".join(sys.argv[1:])

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(SOCKET_PATH)
client.send(msg.encode())
print("💬 Sent:", msg)
response = client.recv(1024)
print("📡 Response:", response.decode())
client.close()
