print('-' * 75)

import traceback as tb

try:
    print(1/1)
    print('string')

    try:
        raise ValueError('Value Cannot be NULL')
    except TypeError as e:
        print(f'TE Occurred: {e}')

except NameError as e:
    print(f'NE Occurred: {e}')
except (ZeroDivisionError, AttributeError) as e:
    print(f'CE Occurred: {e}')
except Exception as e:
    print(f'Error Occurred - {e.__class__.__name__}: {e}')
    print(tb.format_exc())

else:
    print('ELSE Block - No Exceptions')

finally:
    print('FINALLY Block - Always be Executed')

print('After Statements')

print('-' * 75)

# Custom Exceptions
class InvalidNumber(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg

    def display_err_msg(self):
        return f'An Error has Occurred: {self.err_msg}'

try:
    num = input('Enter Any Number between 1 and 9 - ')
    if num.isdigit():
        num = int(num)

        if num in range(1, 10):
            print('Valid Input -', num)
        else:
            raise InvalidNumber('Number should be between 1 and 9')
    else:
        raise InvalidNumber('Input should contain only Numbers')

except InvalidNumber as e:
    print(e.display_err_msg())

print('-' * 75)

def func():
    try:
        print(1/1)
        return 1
    except Exception as e:
        print(f'{e}')
    finally:
        return 2

print('Function Returns -', func())

print('-' * 75)
