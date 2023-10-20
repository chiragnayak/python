'''
Whenever any module is imported, it will be checked in the following directories in the same order:

a) Current Directory
b) PYTHONHOME/lib
   PYTHONHOME/lib/site-packages
c) Temporary Change => sys.path
   Permanenet Change => PYTHONPATH
'''

import sys
print('sys.path -', type(sys.path))

#module_dir = r'D:\Trainings\Python_vmWare\March2021_2\Day_3_24March2021\modules'
#sys.path.insert(0, module_dir)

for path in sys.path:
    print('Path -', path)

import vmware_utils as vu
from vmware_utils import InvalidNumber

print('-' * 75)

print('Mobile Number -', vu.validate_mobile_number('9876543210'))
print('SQR -', vu.sqr(25))

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
