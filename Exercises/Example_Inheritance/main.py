from Exercises.Example_Inheritance.employee import Employee
from Exercises.Example_Inheritance.person import Person

if __name__ == "__main__":
    print('Entering main')
    print('---------------------------------------------------------')
    person1 = Employee('Khan', 'Nakib', 'Employee43046721')
    person1.isEmployee()
    print('---------------------------------------------------------')
    person2 = Person('Khan', 'Ashna')
    person2.isEmployee()
    print('---------------------------------------------------------')

    person1.changeLastName('Smith')
