def power_func(num, power=2):
    return num ** power


print("power_func ", type(power_func))
print("power_func call 1:  ", power_func(3))

"""
lambda functions are nameless functions
single liner functions
can take any number of parameters in any form
it evaluates only one expression (valid single line expression)
evaluated expression will be returned to the caller by default (no need ot return statement)

x = lambda <parameters> : <expression>
"""

calc_lambda = lambda num, power=2: num ** power

print("calc_lambda type : ", calc_lambda, "-", type(calc_lambda))
print("calc_lambda call 1 : ", calc_lambda(5, 3))

"""
OOPS

Empty class:

class Employee(object):
class Employee():
class Employee:

all above are valid
"""


class Employee(object):

    COMPANY = "ARROWHEADS INC."

    def __init__(self, name, loc="Pune", sal=50000):
        self.name = name  # public
        self.loc = loc  # public
        self.__salary = sal  # private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, sal):
        if sal > 0:
            self.__salary = sal
        else:
            print("Salary cannot be zero. Nothing is free!")

    def inc_salary(self, sal):
        if sal > 0:
            self.__salary = self.__salary + sal
        else:
            print("Increment cannot be zero. Dil Maange more!")

    @staticmethod
    def company_name():
        return Employee.COMPANY

    @classmethod # ???? what is the difference ????
    def company_name_v2(self):
        return self.COMPANY

    def __str__(self):
        return f"{self.name} from {self.loc}"


if __name__ == "__main__":
    e = Employee("Raju")
    e.set_salary(0)
    print (Employee.company_name())
    print(e.company_name_v2())
    print(e)
