import os
import time

# This program is intended to remove numbers and numbers and charecters like - _ from the list found in a folder 
def renameFiles():
    time.sleep(2)
    # Step 1 : 'r' indicates python to take the address as it is in raw format
    # Step 2 : get the list and store it in an array list
    folderLocation = r"C:\Users\Naveen Senapathi\Downloads\Naruto Images"
    thelist = os.listdir(folderLocation)
    print(thelist)
    os.chdir(folderLocation)
    deletedigits = str.maketrans(dict.fromkeys("_1234567890- "))
    for each_fileName in thelist:
       # string.translate(table, "the charecters to be removed"), and here
       # table is None
        time.sleep(2)
        os.rename(each_fileName, each_fileName.translate(deletedigits))

renameFiles()
