#! /usr/bin/python3

import sys
from ssh_library import SSH

# Dictionary to simulate different users
users = {
    "root": "toor",
    "user1": "1user",
    "user2": "2user"
}

# Files initially present in the folder structure
files = {"test.py", "test1.py"}

a = SSH(files=files, users=users, system="linux")

if __name__ == "__main__":
    # If no arguments are provided the program will login for root user
    if len(sys.argv) == 1:
        a.login_root(tries=3)
        
    # If username and password are provided the program will try to login to that user
    elif len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        a.login_user(username, password)
    else:
        print("Incorrect number of arguments provided! Expected two arguments")