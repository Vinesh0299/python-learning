def list_files(set_name):
    """Function lists the name of files spanning over 4 columns

        ARGS

            set_name: A set of strings simulating files in folder
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

        ARGS

            set_name: A set of strings simulating files in folder
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

        ARGS

            set_name: A set of strings simulating files in folder
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