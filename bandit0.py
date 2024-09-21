from pwn import *

host = "bandit.labs.overthewire.org"
port = 2220

username = "bandit0"
password = "bandit0"

def basic_reconnaissance(remote_connection):
    shell_output = remote_connection.ls("-l")
    print(shell_output.decode())

def collect_password(remote_connection):
    flag = False
    password = ""
    shell_output = remote_connection.cat("readme")
    formatted_output = shell_output.decode()
    for char in formatted_output:
        if char == ":":
            flag = True
        if char != " " and flag == True:
            password += char
    return password

if __name__ == "__main__":
    connection = ssh(username, host, port, password)
    if connection.connected():
        basic_reconnaissance(connection)
        next_level_password = collect_password(connection)
    connection.close()

    print(f"The password for the next level is: {next_level_password}")

