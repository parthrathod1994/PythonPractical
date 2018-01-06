import socket
print("Enter Port No:")
port = int(input())
#print("enter your message:")
#message = str(input())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

s.bind((host, port))

s.listen(5)

c, addr = s.accept()
print("Connection Establish From"+str(addr))

while True:
    print("enter your message:")
    message = str(input())
    c.send(message.encode())
#data = c.recv(1024).decode('ascii')
#print("Data From Client"+data)
    #print("Enter Your Message:")
    #message = input()


c.close()