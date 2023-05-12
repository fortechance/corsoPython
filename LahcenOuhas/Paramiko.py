# script to connect to a Cisco device and run commands
# by John Kull
from filecmp import*
host1 = '192.168.200.10'
user = 'admin'
secret = 'P@ssword'
port = 22
ssh = filecmp.SSHClient()
ssh.set_missing_host_key_policy(filecmp.AutoAddPolicy()) 
ssh.connect(hostname=host1, username=user, password=secret, port=port)
stdin, stdout, stderr = ssh.exec_command('show clock')
list = stdout.readlines()
print(list)