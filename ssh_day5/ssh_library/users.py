from .utils import ceaser_cipher
from .utils import DEFAULT_SHIFT

class Users:
    """Stores user info"""

    def __init__(self, username, password):
        self._username = username
        self._password = ceaser_cipher(password, DEFAULT_SHIFT)


    def login_user(self, username, password):
        """Function logs in user and send appropriate response depending on input
        
            ARGS:
                username: Username of the user
                password: unencrypted password of user   
        """
        if username != self._username:
            return ("Incorrect username", 403)

        if ceaser_cipher(password, DEFAULT_SHIFT) != self._password:
            return ("Incorrect password", 403)

        return (username, 200)