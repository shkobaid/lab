import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call the remote function

num1=int(input("ENter number 1: "))
num2=int(input("Enter number 2: "))
result = proxy.add(num1, num2)
print("Result from server:", result)

'''
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    msg = input("Enter operation (e.g., add 5 3) or 'exit': ")
    client_socket.send(msg.encode())
    if msg.lower() == "exit":
        break
    result = client_socket.recv(1024).decode()
    print("Result from server:", result)

client_socket.close()'''
