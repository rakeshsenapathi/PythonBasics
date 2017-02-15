try:
    
    f = open("FlatDetails.txt", "r")

    for line in f.readlines():
        if( "Occupied" in line):
            print(line)
        elif( "Vacant" in line):
            print(line)
    f.close()
    
except IOError:
    
    print("File not found!")
    

