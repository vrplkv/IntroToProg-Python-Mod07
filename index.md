# Title
**Dev:** Vera 
**Date:** *8.24.2021*

## Introduction
This github pages details Assignment07 from IT FDN 110 A.
The task was to create a script that demnstrates pickling and structured error handling. 

## Pickling
Pickling, also called marshalling or flattening, is used to serialize or de-serialize python objects such as booleans, integers, floats, strings, tuples, lists, sets and dictionaries. This means storing the data in a binary format instead of plain text.
```
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
```

### Useful links
https://www.datacamp.com/community/tutorials/pickle-python-tutorial

https://www.tutorialspoint.com/python-pickling

## Structured Error Handling
Structured error handling allows you to define your own code for the errors that python code throws, often called exceptions. 
```
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
```

### Useful links
https://www.python-course.eu/python3_exception_handling.php

## Summary
Assignment07 demonstrates the use of pickling and structured error handling.
