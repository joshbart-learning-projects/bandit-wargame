from pwn import *

bandit_host = "bandit.labs.overthewire.org"
bandit_port = 2220

level_username = "bandit0"
level_password = "bandit0"

if __name__ == "__main__":
    connection = ssh(level_username, bandit_host, bandit_port, level_password)
    shell = connection.shell("/usr/bin/bash")
    shell.sendline(b"ls -l")
    shell.sendline(b"exit")
    shell_output = shell.recvall()
    connection.close()

    printable_output = repr(shell_output)
    print(printable_output)

    
    # next_level_password = shell.readline().decode()
    # print(f"The password for the next level is: {next_level_password}")

