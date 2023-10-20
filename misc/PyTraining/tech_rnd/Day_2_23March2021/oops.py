# Class => A template which is a collection of attributes (variables and methods)
# Object => An instance of a class

'''
class Employee(object):
    pass
    
class Employee():
    pass
    
class Employee:
    pass
'''
class Employee(object):
    ename = 'justin'
    eloc = 'blr'

    # Initialize the object
    def __init__(self, name, loc='mumbai', team='testing', sal=5000):
        self.ename = name
        self.eloc = loc
        self.eteam = team
        self.__esal = sal
        print("object initialized -", self)

    # Displays the object in string format
    def __str__(self):
        return f'{self.ename} from {self.eloc} earns Rs.{self.__esal}'

    # Get the Salary
    def get_salary(self):
        return self.__esal

    # Increment the Salary
    def incr_salary(self, amount):
        self.__esal += amount
        return self.__esal

    # Display the details
    @staticmethod
    def display_details():
        return f'{Employee.ename} from {Employee.eloc}'

    # Display the employee details
    @classmethod
    def display_emp(self):
        return f'{self.ename} from {self.eloc}'

if __name__ == '__main__':
    print('-' * 75)

    # Create the objects
    print('Creating Object 1')
    obj_1 = Employee('tris', sal=15000)

    print('Creating Object 2')
    obj_2 = Employee('clark', team='development')

    print('-' * 75)

    # Display the objects
    print('Name of the Module -', __name__)
    print('Object 1 -', obj_1)
    print('Object 2 -', str(obj_2))

    print('-' * 75)

    # Access ename
    print('Name Using Class -', Employee.ename)
    print('Name Using Object 1 -', obj_1.ename)
    print('Name Using Object 2 -', obj_2.ename)

    # Modify ename
    obj_1.ename = "Clark Tris"

    print('-' * 75)

    # Access salary
    print('Object 1 Salary -', obj_1.get_salary())
    print('After Increment 10K -', obj_1.incr_salary(10000))
    print('Updated Object 1 -', obj_1)

    print('-' * 75)

    # Access Display Details
    print('Using Class -', Employee.display_details())
    print('Using Object 1 -', obj_1.display_details())

    print('-' * 75)

    # Access Employee Details
    print('Employee Details using Object 1 -', obj_1.display_emp())

    print('-' * 75)
