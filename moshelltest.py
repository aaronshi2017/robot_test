import paramiko
paramiko.util.log_to_file('paramiko.log')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost', username='aaron', password='aar93onshi3238')
command="ll"

stdin, stdout, stderr = ssh.exec_command(command)
return_code = stdout.channel.recv_exit_status()


# chan = ssh.get_transport().open_session()

# Execute thecommand
# chan.exec_command(r'/home/rantechdev/moshell/moshell 169.254.2.2')
# print(chan.recv_exit_status()) # This will print its return code


if return_code == 0:
    print('Command executed successfully', return_code)
    print(stdout)
else:
    print('Command failed with return code:', return_code)
ssh.close()
