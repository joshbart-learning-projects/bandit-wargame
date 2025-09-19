import logging
from pwn import *

logging.basicConfig(format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s", filename="./var/log/bandit0-$(date +'%Y-%m-%d').log")
logger = logging.getLogger(__name__)

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
    logger.info("Initiating connection to the bandit server...")
    logger.debug(f"Variable value - host: {host}")
    connection = ssh(username, host, port, password)
    if connection.connected():
        logger.info("Connection established successfully.")
        basic_reconnaissance(connection)
        next_level_password = collect_password(connection)
    connection.close()

    print(f"The password for the next level is: {next_level_password}")

