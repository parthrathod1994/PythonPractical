import socket
print("Enter Port no:")
port = int(input())
#print("Enter Your Message:")
#message = str(input())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

s.connect((host, port))

#s.send(message.encode())
while True:
    data = s.recv(1024).decode("ascii")
    print("Data from Server:"+data)

s.close()