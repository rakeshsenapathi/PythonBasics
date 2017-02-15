class Employee():

    Emp_count = 0

    def __init__(self,name,location,salary):
        Employee.Emp_count += 1
        self.name = name
        self.location = location
        self.salary = salary
        if( salary < 50000 ):
            self.salary = self.salary + 5000
        

    def getdetails(self):
            print("Name : %s  Location : %s Salary : %d" %(self.name,self.location,self.salary))

    def getcount(self):
            print("Total Employees %d" %Employee.Emp_count)

obj1 = Employee("Rakesh","Vizag",70000)
obj2 = Employee("Ramesh","Hyderabad", 20000)

obj1.getdetails()
obj2.getdetails()

obj1.getcount()



    
