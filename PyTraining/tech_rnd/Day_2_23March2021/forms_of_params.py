print('-' * 75)

def display_emp(name, loc='bangalore', sal=5000):
    return f'{name.upper()} from {loc.upper()} earns Rs.{sal}'

print('positional (fixed)')

# Based on the position, the values will be assigned to the respective parameter
# Order of parameters should not be changed
print(display_emp('justin', 'pune', 5000))
# print(display_emp('pune', 5000, 'justin'))            # throws error

print('-' * 75)

print('keyword')

# Based on the keyword, the values will be assigned to the respective parameter
# Order of parameters can be changed
print(display_emp(name='tris', loc='mumbai', sal=9000))
print(display_emp(loc='mumbai', sal=9000, name='tris'))

print('-' * 75)

print('mix of positional and keyword parameters')

# Positional Parameters followed by Keyword Parameters
print(display_emp('manual', sal=9000, loc='delhi'))

print('-' * 75)

print('default parameters')

# Parameters can be given the default values in the function definition
# Non-default parameters followed by default parameters
# Parameters which has default values are optional to pass
print(display_emp('damien'))
print(display_emp('damien', sal=9000))

print('-' * 75)

print('variable length parameters')

# *args => 'n' no: of positional params => tuple
# **kwargs => 'n' no: of keyword params => dictionary

def display_det(lang, *scr, platform, **det):
    print('lang -', lang)
    print(scr, '-', type(scr))
    print(det, '-', type(det))
    print('platform -', platform)

    if 'typ' in det:
        print('Type -', det['typ'])

display_det('python',
            'php',
            'perl',
            typ='interpreted',
            name='scripting',
            platform='multi')

print('-' * 75)

display_det('python', platform='multi')

print('-' * 75)

print('Hello')
print('Hello', 'People')
print('Hello', 'People', 'Welcome', 'to', 'Training')

print('-' * 75)
