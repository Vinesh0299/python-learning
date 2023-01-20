import sys
from ssh_library import SSH, Users
from ssh_library.utils import USERS_FOR_TESTING

# initializing user dictionary
# stores user info as username: User class object
users = {}

# creating user objects from dictionary defined in utils.py
for username, password in USERS_FOR_TESTING.items():
    users[username] = Users(username, password)

username = sys.argv[1]
machine_identifier = sys.argv[2]

if username not in users.keys():
    raise ValueError("User does not exists!")

password = input("Enter Password: ")

if users[username].login_user(username, password)[1] == 200:
    ssh_session = SSH(users, machine_identifier)
    ssh_session.ssh_terminal(users[username])
else:
    print("Incorrect password! Login Failed")