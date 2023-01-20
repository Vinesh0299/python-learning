import os
from .utils import DEFAULT_FOLDER_STRUCTURE

class SSH:
    """Provides a structure for ssh connection to a system"""

    def __init__(self, users, identifier="default"):
        self._users = users
        self._identifier = identifier

        self.initialize_folder_structure()


    def initialize_folder_structure(self):
        """Function initializes the folder structure for remote system
            starting from current directory"""
        if self._identifier not in os.listdir():
            os.mkdir(self._identifier)

            # Initializing the folder structure for the new system
            _ = [os.mkdir('{}/{}'.format(self._identifier, folder)) for folder in DEFAULT_FOLDER_STRUCTURE.keys() if DEFAULT_FOLDER_STRUCTURE[folder]['type'] == 'folder']
            _ = [os.mkdir('{}/usr/{}'.format(self._identifier, user)) for user in self._users.keys()]

            # Creating an empty file to store command execution history
            with open("{}/history".format(self._identifier), "w") as f:
                pass


    def clean_up(self):
        """Deletes the initialized folder structure and makes it so that
            the system never existed"""

        print("Cleaning up....")
        _ = os.system("rm -r {}/{}".format(os.getcwd(), self._identifier))


    def get_current_dir(self):
        return os.path.join(os.getcwd(), self._rel_dir)


    def write_history_file(self, command):
        """Creates and maintains the file that stores the previously used
            commands on the system

            ARGS:
                command: Executed command    
        """
        with open(os.path.join(os.getcwd(), "{}/history".format(self._identifier)), "at") as file:
            file.write(command + "\n")


    def set_important_variables(self, user):
        """Set relavent variables when changing user"""

        if user._username == 'root':
            self._rel_dir = "{}/root".format(self._identifier)
        else:
            self._rel_dir = "{}/usr/{}".format(self._identifier, user._username)


    def ssh_terminal(self, user):
        """Function simulates the command line interface of a remote system
        
            ARGS:
                user: an instance of 'user' class
        """
        self.set_important_variables(user)

        print("User logged in! Type 'exit' to turn off terminal\n")

        while True:
            command = input("{}@{}$ ".format(user._username, self._identifier)).strip()

            self.write_history_file(command)

            command_split = command.split()

            if len(command_split) == 1:
                if command.lower() == "exit":
                    cleanUp = input("Do you want to delete the system? (Y/N) ").lower()
                    if cleanUp == "y" or cleanUp == "yes":
                        self.clean_up()
                    print("Logging out")
                    break
                elif command == "whoami":
                    print(user._username)
                elif command == "pwd":
                    print("/{}".format(self._rel_dir))
                elif command == "ls":
                    os.system("ls {}".format(self.get_current_dir()))
                elif command == "history":
                    os.system("tail -100 {}/history".format(self._identifier))
                else:
                    print("unknown command!")
            elif len(command_split) == 2:
                if command_split[0] == "su":
                    username = command_split[1]
                    if username in self._users.keys():
                        password = input("Enter user password: ")

                        if self._users[username].login_user(username, password)[1] == 200:
                            self.ssh_terminal(self._users[username])
                            self.set_important_variables(user)
                        else:
                            print("Incorrect password! Login Failed")
                    else:
                        print("User does not exist!")
                elif command_split[0] == "cd":
                    directory = command_split[1]

                    if directory == ".":
                        pass
                    elif directory == ".." and self._rel_dir == "":
                        pass
                    elif directory == "..":
                        path = self._rel_dir.split('/')
                        self._rel_dir = "/".join(path[:-1])
                    elif directory == "/":
                        self._rel_dir = ""
                    elif directory[0] == "/":
                        self._rel_dir = directory[1:]
                    elif len(self._rel_dir) > 0 and directory in os.listdir(self._rel_dir) and os.path.isdir(os.path.join(self.get_current_dir(), directory)):
                        self._rel_dir += "/{}".format(directory)
                    elif directory in os.listdir() and os.path.isdir(os.path.join(self.get_current_dir(), directory)):
                        self._rel_dir = directory
                    else:
                        print("Folder not present in current directory")
                elif command_split[0] == "cat":
                    directory = command_split[1]

                    if os.path.isfile(os.path.join(self.get_current_dir(), directory)):
                        os.system("cat {}/{}".format(self.get_current_dir(), directory))
                        print("")
                    else:
                        print("{} is not a file".format(directory))
                else:
                    print("Unknown Command")
            else:
                print("Unknown Command")