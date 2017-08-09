try :

    f = open("Skillset.txt", "r")

    count = 0
    
    designation = input("Search the designation:  ")

    for line in f.readlines():
        if(designation == "DEVELOPER"):
           if(designation in line):
              print(line)
              count+=1
    f.close()
    print("Searched Designation Count : %d" %count)

except IOError:
    print("File not Found!")
