# Programme Test pour Jenkins

import paramiko

# Paramètres de connexion ssh
hostssh = 'vmlinux01'
userssh = 'admin'
pwdssh = '@dm1n'

def connectssh(host,username,password):
    cnxssh = paramiko.SSHClient()
    cnxssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    cnxssh.load_system_host_keys()

    try:
        print('creating connection')
        cnxssh.connect(host, username=username, password=password)
        print('connected')
        # yield cnxssh
    finally:
        print('closing connection')
        cnxssh.close()
        print('closed')

# Programme principal
if __name__ == '__main__':
    print('Début du Programme')
    cnx1 = connectssh(hostssh,userssh,pwdssh)

