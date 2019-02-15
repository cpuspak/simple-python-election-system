#client user reg partial

import socket
import threading


def register(sock):
	info = sock.recv().decode('utf-8')
	print(info)
	repeatFlag = 1
	while(repeatFlag):
		userInfo = input()
		password = userInfo.strip().split()[1].encode('base64','strict')
		sock.send(userInfo.strip().split()[0]+" "+password.encode('utf-8'))
		userInfo = sock.recv.decode('utf-8')
		if(userInfo.strip().split()[1] == "successful"):
			repeatFlag = 0
			print(userInfo)
		else:
			repeatFlag = input("Wish to try again (1/0): ")

def Main():
	host = "Server ip"
	port = 63

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((host,port))
		print("Connected to ("+host+":"+str(port)+")...")
		register(sock)
	except:
		print("Server down...")

if __name__ == '__main__':
	Main()


