import socket 
d= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip ='192.168.43.114'
port = 5001

sender2 = ('192.168.43.114',5000)
d.bind((ip,port))
#n = int(input('enter no of messages'))

for i in range(0,3):
    message =input('->')
    d.sendto(message.encode('utf-8'),sender2)
while(True):
    data,addr = d.recvfrom(1024)
    print('Recieved from the sender2',str(data))
    message = input('-->')
    d.sendto(message.encode('utf-8'),sender2)  
    
    
