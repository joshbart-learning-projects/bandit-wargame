from pwn import *

bandit_host = "bandit.labs.overthewire.org"
bandit_port = 2220

level_username = "bandit1"
level_password = "NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL"

if __name__ == "__main__":
    ssh_connection = ssh(level_username, bandit_host, bandit_port, level_password)
    shell = ssh_connection.shell()

    
    sh.sendline(b"pwd")
    print(sh.recvuntil(b"bandit").decode())



    # sh.sendline(b"ls -l")
    # sh = shell.system("ls -l")
    # print(sh.recvline().decode())
    # sh.clean()
    # sh.interactive()
    shell.close()