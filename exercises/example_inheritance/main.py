from exercises.example_inheritance.employee import Employee
from exercises.example_inheritance.person import Person

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
