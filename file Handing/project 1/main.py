from pathlib import Path

def readfileandfolder():
    path = Path(".")                        # Path(".") means the current directory
    items = list(path.rglob('*'))           # Find all files and folders recursively
    for i, items in enumerate(items):       # Display each file/folder with a number
        print(f"{i+1} : {items}") 


def createfile():
    try:
        readfileandfolder()
        fileName = input("Write File name or create a new one :")
        p = Path(fileName)      #create a path object using the filename entered by the user 
        if not p.exists():
            with open(p,'w') as fs:
                data = input("write some data in this file : ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already Exist!")

        

    except Exception as err:
        print(f"an error occured as {err}")

    


print("Press 1 for creating a file : ")
print("Press 2 for reading a file : ")
print("Press 3 for updating a file : ")
print("Press 4 for deleting a file : ")

check = int(input("Tell your Response : "))

if check == 1:
    createfile()
