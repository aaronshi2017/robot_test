try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    import paramiko
    ROBOT = False
except Exception:
    ROBOT = False

class class_moshellcommand:
    # define the class variants
    defaultcommand=[]
    host="localhost"
    username="aaron"
    password='aar93onshi3238'
    output=""
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    

    def __init__(self):
        # Automatically add the host key if not present
        paramiko.util.log_to_file('paramiko.log')
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
             # Connect to the SSH server
            self.ssh_client.connect(self.host, username=self.username, password=self.password)
            print("SSH connection is successful!")
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
        except paramiko.SSHException as e:
            print("Unable to establish SSH connection:", str(e))
        finally:
            pass
    
    def commandexecution(self,command):
        print(command)
        #Input command should be a list 
        self.defaultcommand.append(command)
        print(self.defaultcommand)
        for command in self.defaultcommand:
            # Run the command
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            
            # Read the output
            return_code = stdout.channel.recv_exit_status()
            output = stdout.read().decode('utf-8')

            # Print the output
            print(f"Output of '{command}':")
            print(output)
            return return_code
    
    @keyword
    def ssh_Close(self):
        try:
            print("SSH connection will be closed!")
            self.ssh_client.close()
            return 0
        except paramiko.SSHException as e:
            print("ssh close has error", str(e))
            return -1
        finally:
            pass
