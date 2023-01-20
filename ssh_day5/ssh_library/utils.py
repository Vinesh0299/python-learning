DEFAULT_SHIFT = 5

DEFAULT_FOLDER_STRUCTURE = {
    'etc': {
        'type': 'folder',
        'childs': []
    },
    'bin': {
        'type': 'folder',
        'childs': []
    },
    'sbin': {
        'type': 'folder',
        'childs': []
    },
    'usr': {
        'type': 'folder',
        'childs': []
    },
    'root': {
        'type': 'folder',
        'childs': []
    },
    'history': {
        'type': 'file'
    }
}

USERS_FOR_TESTING = {
    "root": "toor",
    "user1": "1user",
    "admin": "admin"
}

def ceaser_cipher(plain_text, shift_positions):
    cipher_text = ""

    for character in plain_text:
        if(ord(character) > ord('A') and ord(character) < ord('a')):
            character = ord(character) - ord('A') + shift_positions
            character = character % 26
            character_new = chr(character + ord('A'))
        else:
            character = ord(character) - ord('a') + shift_positions
            character = character % 26
            character_new = chr(character + ord('a'))

        cipher_text += character_new

    return cipher_text