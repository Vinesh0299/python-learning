import random
from .helper_functions import list_files, remove_file, create_file

class SSH:
    """Provides a re-usable block of implementation for ssh"""

    def __init__(self, files, users, system="linux"):
        self._folder = files
        self._users = users
        self._system = system


    def login_root(self, tries=3):
        """Function is used for root user login only"""

        while tries > 0:
            passwd = input("Please enter password for user 'root': ")

            if passwd != self._users["root"]:
                tries -= 1
                if tries == 0:
                    print("Login Attempt failed!")
                else:
                    print("Incorrect password! Try again!")
            else:
                self.ssh_terminal("root")
                break


    def login_user(self, username, password):
        """Function is used for user login"""

        if username not in self._users.keys():
            raise ValueError("Username does not exists")

        if self._users[username] == password:
            self.ssh_terminal(username)
        else:
            print("Incorrect password!")


    def ssh_terminal(self, user="root"):
        """Function simulates the execution of commands on remote server.
            It takes two arguments 'user' and 'system' both defaults to 'root'
            and 'linux' respectively.

            These arguments are used to create the user and system identifier in
            the command line interface
        """

        print("Connection Established!! Type 'exit' to break the connection. Type 'help' to list the available commands")
        print("")
        while True:
            command = input("{}@{}:/# ".format(user, self._system))

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
                list_files(self._folder)
            elif command == "create":
                create_file(self._folder)
            elif command == "delete":
                remove_file(self._folder)
            else:
                print("Invalid command, try again!")
            print("")