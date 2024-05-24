from pwn import *

bandit_host = "bandit.labs.overthewire.org"
bandit_port = 2220

level_username = "bandit0"
level_password = "bandit0"

def basic_reconnaissance(remote_connection):
    shell = remote_connection.shell()
    shell.sendline(b"ls -l")
    shell.sendline(b"exit")
    shell_output = shell.recvall()
    print("Initial login and filesystem info:\n\n")
    print(shell_output.decode())

if __name__ == "__main__":
    connection = ssh(level_username, bandit_host, bandit_port, level_password)
    if connection.connected():
        basic_reconnaissance(connection)
    connection.close()

    # next_level_password = shell.readline().decode()
    # print(f"The password for the next level is: {next_level_password}")

