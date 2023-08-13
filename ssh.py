from fabric import Connection
from paramiko import SSHClient


host = '141.8.199.177'
user = 'root'
password = 'mazuexdeefseuh'
port = 22

client = SSHClient(host=host, port=port, user=user, password=password)
shell = client.invoke_shell()

# client = Connection(host=host, 
#                     user=user, 
#                     port=port, 
#                     connect_kwargs={'password': password})


# while True:
#     cmd = input('<command-> ')
#     if cmd == '__QUIT__':
#         print('QUITTING')
#         break
#     else:
#         res = client.run(cmd).stdout
#         print(res)

print(client.run('ls;cd venv; ls').stdout)
