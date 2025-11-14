from xmlrpc.server import SimpleXMLRPCServer

# Define a function to expose
def add(x, y):
    return x + y

# Create RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server running on port 8000...")

# Register the function
server.register_function(add, "add")

# Run the server
server.serve_forever()

'''
import socket

def process_request(request):
    parts = request.strip().split()
    if len(parts) != 3:
        return "Invalid request"
    op, a, b = parts[0], int(parts[1]), int(parts[2])
    if op == "add":
        return str(a + b)
    elif op == "sub":
        return str(a - b)
    elif op == "mul":
        return str(a * b)
    elif op == "div":
        return str(a // b if b != 0 else "Error: Divide by zero")
    else:
        return "Unknown operation"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("RPC Server running on port 12345...")

client_socket, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    data = client_socket.recv(1024).decode()
    if not data or data.lower() == "exit":
        break
    result = process_request(data)
    client_socket.send(result.encode())

client_socket.close()
server_socket.close()'''
