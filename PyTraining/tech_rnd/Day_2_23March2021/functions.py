print('-' * 75)

# Functions
# Re-usable piece of code
def validate_mobile_number(mobile):
    status = 'invalid'

    '''
    Should be 10 Digits
    First digit should be between 6 and 9
    '''
    if len(mobile) == 10 and mobile.isdigit() and int(mobile[0]) in range(6, 10):
        status = 'valid'

    return status, len(mobile), [mobile, mobile.isdigit()]

print(validate_mobile_number, '-', type(validate_mobile_number))
ret_status = validate_mobile_number('8876543210')
if ret_status is not None:
    print('Returns -', ret_status, '-', type(ret_status))
else:
    print("Function Returns Nothing")

print('-' * 75)

name = 'justin'
loc = 'bangalore'
sal = 9000.508776

print('Concat -', name + ' from ' + loc + ' earns Rs.' + str(sal))
print('Format 1 -', '{} from {} earns Rs.{}'.format(name, loc, sal))
print('Format 2 -', '{} from {} and {} earns Rs.{}'.format(name, loc, name, sal))
print('Format 3 -', '{0} from {1} and {0} earns Rs.{2}'.format(name, loc, sal))
print('Format 4 -', '{nm} from {lc} earns Rs.{sl}'.format(nm=name,
                                                          lc=loc,
                                                          sl=sal))

print('Format 5 -', f'{name.upper()} from {loc.title()} earns Rs.{sal + 25000}')
print('Format 6 -', '%s from %s earns Rs.%.02f' % (name, loc, sal))
print('Using Padding 1 -', '{:10} from Bangalore'.format(name))
print('Using Padding 2 -', '{:>10} from Bangalore'.format(name))

print('-' * 75)
