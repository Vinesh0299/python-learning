import random

tries = 0
file_number = 1
password = "test"

folder = ["ssh.py", "test.py"]

while tries < 3:
    passwd = input("Please enter password for user 'root': ")

    if passwd != password:
        tries = tries + 1
        if tries == 3:
            print("All attemps to login failed, breaking the connection")
        else:
            print("Incorrect Password! try again!")
    else:
        print("Connection Established!! Type 'exit' to break the connection. Type 'help' to list the available commands")
        print("")
        while True:
            command = input("Enter Command: ")

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

        break