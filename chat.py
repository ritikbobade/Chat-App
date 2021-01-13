import socket
import threading
import os
ip  =  "Current_system_ip"
port = 1234
s = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
s.bind( (ip,port) )

os.system('clear')
#taking reciever info
host_ip = input("Enter the IP of reciever: ")
host_port = int(input("Enter the Port of the reciever: "))

os.system('tput setaf 3')
os.system("echo '<Chit Chat> App' | figlet")


#defining recieving function
def recieve():
        while(True):
                os.system('tput setaf 6')
                recv_data = s.recvfrom(2048)
                print("    ", recv_data[0].decode())

#defining sending function
def send():
        while(True):
                data = input()
                os.system("tput setaf 5")
                s.sendto(data.encode(), (host_ip,host_port))
                if ('bye' in data ):
                        os.system('tput setaf 7')
                        os._exit(1)


os.system('tput setaf 7')

#defining threads
x1 = threading.Thread( target=recieve )
x2 = threading.Thread( target=send )

#Starting Threads
x1.start()
x2.start()