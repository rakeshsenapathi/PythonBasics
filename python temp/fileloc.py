
try:

    productType = "Soaps"
    
    f = open("ProductLocations.txt", "r")
    
    for each_line in f.readlines():
        if( productType in each_line ):
            print(each_line)
            f.close()

except IOError:
    f.close()
    print("Cant be found")





    
