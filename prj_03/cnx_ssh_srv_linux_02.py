# Programme Test pour Jenkins

import paramiko

# Paramètres de connexion ssh
hostssh = 'vmlinux01'
userssh = 'admin'
pwdssh = '@dm1n'

# Fonction de connexion ssh au serveur distant
def connectssh(hostssh, userssh, pwdssh):
	cnxssh = paramiko.SSHClient()
	cnxssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
	cnxssh.load_system_host_keys()
	cnxssh.connect(hostssh, username=userssh, password=pwdssh)

	print('Connexion ssh au serveur {} initiée ...'.format(hostssh))
	print('User de connexion : {}'.format(userssh))

	# Listes des commandes à exécuter
	commands = ['cd /home/admin/tests','pwd','ls -rtl','echo "test_01" > test_01.log','ls -rtl']
	command = str('')
	for x in commands:
		command += x + '\n'

	stdin, stdout, stderr = cnxssh.exec_command(command)

	for x in stdout:
		print(x)

	cnxssh.close()

# Programme principal
if __name__ == '__main__':
	print('Début du Programme')
	cnx1 = connectssh(hostssh,userssh,pwdssh)

