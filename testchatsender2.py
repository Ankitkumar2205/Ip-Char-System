import socket
ip = '192.168.43.114'
port = 5000
d =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
d.bind((ip,port))
print('server started')
sender1 =('192.168.43.114',5001)

while(True):
    for i in range(0,10):
        data,addr = d.recvfrom(1024)
        print('recieving data from sender 1')
        print(str(data),addr)
        print('sending data to sender1')
       
        message = input('->')
        d.sendto(message.encode('utf-8'),sender1)
       
