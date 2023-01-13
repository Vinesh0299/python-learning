#! /usr/bin/python3

import sys
import random

# Dictionary to simulate different users
users = {
    "root": "toor",
    "user1": "1user",
    "user2": "2user"
}

def list_files(set_name):
    """
        Function lists the name of files spanning over 4 columns

        PARAMETERS

            set_name - A set of strings simulating files in folder
    """

    print("Files inside this current directory are: \n")

    # Printing out the name of all the existing files
    for i in range(0, len(set_name), 4):
        print('\t\t'.join(list(set_name)[i:i+4]))
        
        if i+4 < len(set_name):
            print("")


def remove_file(set_name):
    """
        Function simulates deletion of a file from a folder.

        PARAMETERS

            set_name  -  A set of strings simulating files in folder
    """

    list_files(set_name)

    print("")

    value = input("Enter name to delete: ")

    print("")

    try:
        set_name.remove(value)

        print("File Deleted successfully!")
    except KeyError:
        print("Entered file name does not exist!")


def create_file(set_name):
    """
        Function simulates creation of a new file in folder

        PARAMETERS

            set_name  -  A set of strings simulating files in folder
    """

    list_files(set_name)

    print("")

    value = input("Name of file: ")

    print("")

    if value in set_name:
        print("File name already exists!")
    else:
        set_name.add(value)
        print("File created successfully!")


def ssh_terminal(user="root", system="linux"):
    """
        Function simulates the execution of commands on remote server.
        It takes two arguments 'user' and 'system' both defaults to 'root'
        and 'linux' respectively.

        These arguments are used to create the user and system identifier in
        the command line interface
    """

    folder = {"ssh.py", "test.py"}

    print("Connection Established!! Type 'exit' to break the connection. Type 'help' to list the available commands")
    print("")
    while True:
        command = input("{}@{}:/# ".format(user, system))

        print("")
        if command == "exit":
            print("Logging out")
            break
        elif command == "help":
            print("Available commands:")
            print("help    -  List all available commands")
            print("random  -  Output a random number between 0 and 100 both inclusive")
            print("ls      -  List all files in current directory")
            print("create  -  Create a new file")
            print("delete  -  Delete a file")
            print("exit    -  Break the connection")
        elif command == "random":
            print('Your random number is: ' + str(random.randrange(101)))
        elif command == "ls":
            list_files(folder)
        elif command == "create":
            create_file(folder)
        elif command == "delete":
            remove_file(folder)
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