# Programme Test pour Jenkins

import paramiko

# Paramètres de connexion ssh
hostssh = 'vmlinux01'
userssh = 'admin'
pwdssh = '@dm1n'

# Connexion ssh au serveru linux distant
cnxssh = paramiko.SSHClient()
cnxssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
cnxssh.load_system_host_keys()
cnxssh.connect(hostssh, username=userssh, password=pwdssh)
stdin, stdout, stderr = cnxssh.exec_command('ls -l')
for x in stdout:
	print(x)

cnxssh.close()

# pour SFTP = transfert !!  => get
# cnxsftp = cnxssh.open_sftp()
# cnxsftp.get('./image001.jpg', './image.jpg')

