#only user registration partially implemented
import sqlite3
import socket
import threading

registrationFormat = "uniqueUserName password" #password in encrypted format

def createTable(tableName,cursor,fields):
	query = "CREATE TABLE "+tableName
	details = "("
	for i in range(len(fields)):
		if(i == 0):
			details += (fields[i] + ',')
		elif(i != len(fields)):
			details += (' '+fields[i]+',')
		else:
			details += (' '+fields[i]+')')
	query += details
	cursor.execute(query)


def inDataBaseUser(userName):
"""
not implemented
"""

def checkRegistrationConstraints(userInfo):
	if(len(userInfo.strip().split()) != 2):
		return (False,"Arguments not given properly")
	elif(inDataBaseUser(userInfo.strip().split()[0])):
		return (False,"Username already registered")
	else:
		insert(userInfo)
		return (True,"Registration successful")

def Register(name, sock, addr):
	sock.send(str.encode("registration format :"+registrationFormat))
	userInfo = sock.recv().decode("utf-8")

	registered = 0

	while(not registered):
		registrationConstraintsInfo = checkRegistrationConstraints(userInfo)
		if(registrationConstraintsInfo[0] == False):
			sock.send(registrationConstraintsInfo[1] + " send agein : ".encode('utf-8'))
		else:
			sock.send(registrationConstraintsInfo[1].encode('utf-8'))
			registered = 1

def startHosting():
	host = socket.gethostbyname('0.0.0.0')
	port = 63
	sock = secket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host,port))
	sock.listen(5)

	print("Server is hosting registration...")

	userRegisterFlag = 1

	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()
	fields = ['username TEXT','password TEXT'] 
	createTable('users.db',cursor,fields)

	while(userRegisterFlag):
		userRegisterFlag = input("Continue registration (0/1) : ")
		c,addr = sock.accept()

		print("Registering user "+"("+str(addr[0])+":"+str(addr[1])+")")
		t = threading.Thread(target = Register, args = ('registration',c,addr))
		t.start()

	sock.close()


def Main():
	count = 0
	while(True):
		hostPoll = input('Host '+str(count)+'th poll ? (y/n): ')
		if(hostPoll == 'y'):
			startHosting()#user registration
			count += 1
		else:
			quit = input('Quit ?(y/n) :')
			if(quit == 'y'):
				break



if __name__ == "__main__":
	Main()