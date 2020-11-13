class Person:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printData(self):
        print("First Namme:",self.fname)
        print("Last Name: ",self.lname)

# obj = Parent("Nitesh","Wayafalkar")
# obj.printData()

# To inherit Parent class Pass the Parent class name in Child class
class Student(Person):
    def __init__(self,fname,lname , year): # Add constructor to child class
        #Person.__init__(self,fname,lname)  # In order use parent class constructor call Parent class constructor
        super().__init__(fname,lname)  # super() will call parent class constructor
        self.graduantionYear = year

    def printDataFromChild(self):
        print("First Name: ",self.fname,"Last Name:",self.lname,"Graduation year :",self.graduantionYear)


student = Student("Nitesh","Wayafalkar",2015)  # to call data members of Parent class through child class ,
                                          # create object of child class
student.printDataFromChild()





