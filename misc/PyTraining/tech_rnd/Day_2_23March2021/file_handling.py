print('-' * 75)

import os

# File Handling
# 3 Primary Modes => r (read => default), w (overwrite), a (append)
# r+, w+, a+, rb, wb, ab, rb+, wb+, ab+

# Function to create a file
def write_file(fname, fmode):
    # Open the file
    fhandle = open(fname, fmode)

    # Get the input from the user
    while True:
        line = input('Enter a Line - ')
        if line.upper() == 'EOF':
            break

        # Write the line to the file
        fhandle.write(f'{line}\n')

    # Close the file
    fhandle.close()

# filename
filename = r'D:\Trainings\Python_vmWare\March2021_2\Day_2_23March2021\files\data.txt'
# write_file(filename, 'w')
print('File Created')

print('-' * 75)

# write_file(filename, 'a')
print('Contents Appended')

print('-' * 75)

# Read the contents of the file
with open(filename) as fread:
    print('File Mode -', fread.mode)
    print('Is File Closed in WITH Block -', fread.closed)

    print('-' * 75)

    # read => reads the number of bytes provided
    print('Read 1 -', fread.read(10))
    print('Read 2 -', fread.read(20))
    print('Read 3 -', fread.read())

    # Move the cursor back to beginning of the file
    fread.seek(0)

    print('-' * 75)

    # readline => stops reads the characters once it reads '\n'
    print('ReadLine 1 -', fread.readline(10))
    print('ReadLine 2 -', fread.readline(20))
    print('ReadLine 3 -', fread.readline())

    # Move the cursor back to beginning of the file
    fread.seek(0)

    print('-' * 75)

    # readlines => reads all the lines in the form of list
    all_lines = fread.readlines()
    print('All Lines -', all_lines)

    print('-' * 75)

print('Is File Closed -', fread.closed)

print('-' * 75)

# Add more lines
all_lines.insert(3, "The Name 'PYTHON' is derived from\n")
all_lines.insert(4, "from \"Monty Python's Flying Circus\"\n")
print('Modified Lines -', all_lines)

# Write the modified contents to a file
with open(r'files/data_modified.txt', 'w') as fwrite:
    fwrite.writelines(all_lines)
print('Data Copied')

print('-' * 75)

# Check for the existence of the file
print('Chk File 1 -', os.path.exists(filename))
print('Chk File 2 -', os.path.isfile(filename))
print('Chk File 3 -', os.access(filename, os.F_OK))
print('Read Permission -', os.access(filename, os.R_OK))
print('Write Permission -', os.access(filename, os.W_OK))
print('Execute Permission -', os.access(filename, os.X_OK))

print('-' * 75)
