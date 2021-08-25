# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Vera,8.23.2021,Created Script
#   Get inputs from user and return as a list
#   Save data to a binary file
#   Read data from a binary file
#   Have user input filename to save and read to/from
#   Add Menu options and call other functions within presentation
#   Error Handling
#       for integer and string inputs
#       .dat file type
#       create file that does not exist with empty list
# Vera,8.24.2021,Add comments to script

# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = None
lstCustomer = []
lstDefault = []

# Processing -------------------------------------- #
class FileNotDATError(Exception):
    """  File extension must end with dat to indicate it is a data file  """
    def __str__(self):
        return 'File extension not dat'

#receive input from user on file name for a dat file type
def enter_file_name():
    try:
        file_name = input("Enter the name of the file you want to use: ")
        if file_name.endswith('dat') == False:
            raise FileNotDATError()
        else:
            pass
    except Exception as e:
        print("There was an error!")
        print(e, e.__doc__, sep='\n')
        file_name = input("Please re-enter file name: ")
    try:
        open(file_name, "r")
    except FileNotFoundError:
        print("File did not exist. But we created one for you!")
        objFile = open(file_name, "x") #create file
        objFile = open(file_name, "wb") # write empty list to new file
        pickle.dump(lstDefault, objFile)
        objFile.close()
    return file_name

#save data to a binary file
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "wb")
    pickle.dump(list_of_data, objFile)
    objFile.close()
    print(list_of_data,"saved to", file_name)

#read data from a binary file
def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    objFileData = pickle.load(objFile)  # load() only loads one row of data.
    objFile.close()
    print(objFileData, "read from ", file_name)
    return objFileData

#Recieve an integer as a user input with error handling to repeat until user provides an integer
def int_input(prompt):
    while True:
        try:
            intId = int(input(prompt))
            return intId
        except ValueError:
            print("Not an integer! Try again")

#Recieve a string as a user input with error handling to repeat until user provides a string
def str_input(prompt):
    while True:
        try:
            strName = str(input(prompt))
            if strName.isnumeric():
                raise Exception('Do not use numbers for the file\'s name')
            return strName
        except Exception:
            print("Not a string! Try again")

#Obtain inputs from user and return as a list
def get_id_and_name():
    intId = int_input("Enter an Id: ")
    strName = str_input("Enter a Name: ")
    lstCustomer = [intId, strName]
    return lstCustomer

#Menu options
def print_Menu_Tasks():
    print("(1) Read from file")
    print("(2) Update inputs")
    print("(3) View current Id and Name")
    print("(4) Save to file")
    print("(5) Exit program")

#Obtain user input on menu selection
def input_menu_choice():
    menu_Choice = input("Which menu item number would you like to select (1-4)? ")
    return menu_Choice

# Presentation ------------------------------------ #
while(True):
    print_Menu_Tasks()  # Shows menu
    menu_Choice = input_menu_choice()  # Get input for menu option from user

    if menu_Choice.strip() == '1':  # Read the data from the file into a new list object and display the contents
        strFileName = enter_file_name()
        lstCustomer = read_data_from_file(strFileName)
        continue
    elif menu_Choice == '2': # Get ID and NAME From user, store as list object
        lstCustomer = get_id_and_name()
        # print(strFileName,lstCustomer)
        continue
    elif menu_Choice == '3':  #Review current ID and Name
        print(lstCustomer)
    elif menu_Choice == '4': # Store the list object into a binary file
        strFileName = enter_file_name()
        save_data_to_file(strFileName, lstCustomer)
        continue
    elif menu_Choice == '5': #Exit the program
        break
    else:
        print("You did not select a menu item (1-4). Please try again. ")
        continue
