#! /usr/bin/python3

import sys
import random

# Dictionary to simulate different users
users = {
    "root": "toor",
    "user1": "1user",
    "user2": "2user"
}

def ssh_terminal(user="root", system="linux"):
    """
        Function simulates the execution of commands on remote server.
        It takes two arguments 'user' and 'system' both defaults to 'root'
        and 'linux' respectively.

        These arguments are used to create the user and system identifier in
        the command line interface
    """
    file_number = 1
    folder = ["ssh.py", "test.py"]

    print("Connection Established!! Type 'exit' to break the connection. Type 'help' to list the available commands")
    print("")
    while True:
        command = input("{}@{}: ".format(user, system))

        print("")
        if command == "exit":
            print("Logging out")
            break
        elif command == "help":
            print("Available commands:")
            print("help - list all available commands")
            print("random - output a random number between 0 and 100 both inclusive")
            print("ls - list all files in current directory")
            print("create - create a new file")
            print("exit - break the connection")
        elif command == "random":
            print('Your random number is: ' + str(random.randrange(101)))
        elif command == "ls":
            print("Files inside this current directory are: ")
            for files in folder:
                print(files)
        elif command == "create":
            print("New file 'Test_{}' created".format(file_number))
            folder.append('Test_{}'.format(file_number))
            file_number += 1
        else:
            print("Invalid command, try again!")
        print("")

if __name__ == "__main__":
    # If no arguments are provided the program will login for root user
    if len(sys.argv) == 1:
        tries = 0

        while tries < 3:
            passwd = input("Please enter password for user 'root': ")

            if passwd != users["root"]:
                tries = tries + 1
                if tries == 3:
                    print("All attemps to login failed, breaking the connection")
                else:
                    print("Incorrect Password! try again!")
            else:
                ssh_terminal("root")
                break
    # If username and password are provided the program will try to login to that user
    elif len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        if username in users.keys() and users[username] == password:
            ssh_terminal(username)
        else:
            print("Incorrect username or password! Please try again!")
    else:
        print("Incorrect number of arguments provided! Expected two arguments")
