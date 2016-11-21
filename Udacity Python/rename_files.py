import os
def renameFiles():
	 # Step 1 : 'r' indicates python to take the address as it is in raw format
	 # Step 2 : get the list and store it in an array list
     thelist = os.listdir(r"F:\Projects\PythonBasics\Udacity Python\prank")
     print (thelist)
     original_path = os.getcwd()
     os.chdir(r"F:\Projects\PythonBasics\Udacity Python\prank")
     deletedigits = str.maketrans(dict.fromkeys("1234567890"))
     for each_fileName in thelist:
     	 #string.translate(table, "the charecters to be removed"), and here table is None
	     os.rename(each_fileName, each_fileName.translate(deletedigits))
	     #os.chdir(original_path)

renameFiles()