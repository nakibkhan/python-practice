from Example_Inheritance.Person import Person

# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    def __init__(self, lastName, firstName, employeeNumber):
        super(Employee,self).__init__(lastName, firstName)
        self.employeeNumber = employeeNumber

    def isEmployee(self):
        print ("This Employee Class has over-ridden the Person Class")
        print 'Name : %s, %s ' % (self.lastName, self.firstName)
        print 'Employee Number : %s' %(self.employeeNumber)
        return True
