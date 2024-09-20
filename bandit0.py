from pwn import *

host = "bandit.labs.overthewire.org"
port = 2220

username = "bandit0"
password = "bandit0"

def basic_reconnaissance(remote_connection):
    shell_output = remote_connection.ls("-l")
    print(shell_output.decode())

if __name__ == "__main__":
    connection = ssh(username, host, port, password)
    if connection.connected():
        basic_reconnaissance(connection)
    connection.close()

    # next_level_password = shell.readline().decode()
    # print(f"The password for the next level is: {next_level_password}")

