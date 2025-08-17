
from pathlib import Path
import os

def readfileandfolder():
    path = Path('')     # gives current directory file path
    items = list(path.rglob('*'))   # gives list of files 
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")




def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name :- ")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input("what you want to wrtie in this file :-  ")
                fs.write(data)
                
            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")
    
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try: 
        readfileandfolder()
        name = input("While file you want to read ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
            print(data)


            print("Readed successfully")

        else:
            print("THe file does not exists")
    
    except Exception as err:
        print(f"An error occured as {err}")

    

def updatefile():
    # change file name
    # append file data
    # overwrite file data

    try: 
        readfileandfolder()
        name = input("tell which file you want to update :- ")
        p=Path(name)


        if p.exists() and p.is_file():
            print("press 1 for changing name of file ")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file ")
            
            res = int(input("Tell your response :- "))


        if res ==1:
            name2 = input("tell your new file name :- ")
            p2 = Path(name2)
            p.rename(p2)

        if res ==2 :
            with open(p,'w') as fs:
                data = input("tell what you want to write, this will overwrite the data :- ")
                fs.write(data)

        if res ==3:
            with open(p,'a') as fs:
                data = input("tell what you want to append :- ")
                fs.write(" "+data)


    except Exception as err: 
        print(f"An error occured : {err}")




def deletefile():

    try: 
        readfileandfolder()
        name = input("which file you want to delete :- ")
        p= Path(name)
        print(p)

        if p.exists() and p.is_file():
            os.remove(p)
        
            print("file removed successfully ")
    
        else:
             print("no such file exists !!!! ")


    except Exception as err:
        print(f"Error occured {err}")

    
   

print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deletion a file")

check = int(input("Please tell your response :- "))

if check == 1: 
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()


if check == 4:
    deletefile()