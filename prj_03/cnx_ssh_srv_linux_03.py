# Programme Test pour Jenkins

import paramiko
import os
from time import sleep
from datetime import datetime

# Paramètres de connexion ssh
hostssh = 'vmlinux01'
userssh = 'admin'
pwdssh = '@dm1n'
portssh = '22'

# Initialisation des Variables
rep = "/home/" + userssh + "/tests"
logfile = "tests_cnxssh.log"

class SSHConnection:
	"""
		Class pour effectuer une connextion SSH via le module paramiko
	"""

	def __init__(self,host,username,password,port):
		paramiko.util.log_to_file('c:\\Temp\\cnx_paramiko.log')
		self.host = host
		self.port = port
		self.username = username
		self.password = password

	def connectssh(self):
		"""
			Connection SSH au serveur distant
		"""
		cnxssh.connect(self.host, username=self.username, password=self.password)
		print('- Connection ssh au serveur {} :\tOK'.format(self.host))

	def deconnectssh(self):
		"""
			Déconnection SSH du serveur distant
		"""
		cnxssh.close()
		print('- Déconnection ssh du serveur {} :\tOK\n'.format(self.host))

	def execcommandssh(self,command):
		"""
			Exécution de commande SSH sur le serveur distant
		"""
		print('- Début d\'excécution des commandes...\n')
		print(command)
		print(20*"-")
		stdin, stdout, stderr = cnxssh.exec_command(command)
		for x in stdout:
			print(x)
		print(20*"-")
		print('- Fin d\'excécution des commandes.')

def temporisation(tempo):
	# Pause de 5 secondes
	print('- Pause de {} secondes'.format(tempo))
	sleep(tempo)

# Programme principal
if __name__ == '__main__':

	print(20*'='+'\nDébut du Programme\n' + 20*'=')

	# Initialisation de la connexion
	cnxssh = paramiko.SSHClient()
	cnxssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
	cnxssh.load_system_host_keys()

	# Déclaration de la Class
	cnx1 = SSHConnection(hostssh,userssh,pwdssh,portssh)

	# Connection au serveur distant
	cnx1.connectssh()

	# Pause de 5 secondes
	temporisation(5)

	# Commandes à exécuter
	horodatage = datetime.now().strftime('%Y%m%d_%H%M%S')
	msglog = horodatage+' - Connection ssh OK'

	listcommandes = ['cd '+rep, 'pwd', 'echo "'+msglog+'" >> '+logfile, 'ls', 'cat '+logfile+' | tail -5' , 'sleep 5']

	command = str('')
	for x in listcommandes:
		command += x + '\n'

	cnx1.execcommandssh(command)

	# Déconnection au serveur distant
	cnx1.deconnectssh()

	print(20*'='+'\nFin du Programme\n' + 20*'=')
