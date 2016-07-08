import paramiko
import platform

def createUser(serverIp,serverPass,username,password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(serverIp, username='root', password=serverPass)
	stdin, stdout, stderr = client.exec_command('useradd -p' +password+ username)
	client.close()

def deleteUser(serverIp,serverPass,username,password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(serverIp, username='root', password=serverPass)
	if("Ubuntu" in platform.dist()[0]):
		stdin, stdout, stderr = client.exec_command('deluser --remove-home'+ username)
       	else:
		stdin, stdout, stderr = client.exec_command('userdel --remove'+ username)
	 client.close()


