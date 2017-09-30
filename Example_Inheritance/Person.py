# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Person(object):
    #Constructor
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def isEmployee(self):
        print('This is the super class Person')
        print('Name : %s, %s ' %(self.lastName, self.firstName))
        return False

    def changeLastName(self, newLastName):
        self.lastName = newLastName
        print('The Last Name for this Person has been changed to %s' %(self.lastName))