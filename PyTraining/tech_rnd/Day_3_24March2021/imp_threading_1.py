print('-' * 75)

# Multithreading => Concurrent Processing
from threading import Thread
from time import sleep
from datetime import datetime

# Function which is getting invoked,
# Whenever the thread is started
def write_file(trd_name, fname, msg, delay):
    print(f'{trd_name} Started')

    # Write the message to the file
    with open(fname, 'w') as fwrite:
        for n in range(1, 6):
            fwrite.write(f'{datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")} => {msg}\n')
            sleep(delay)

    print(f'{trd_name} Ended')

# Create the Threaded Objects
trd1 = Thread(target=write_file, args=('T1', r'files\t1_out.txt', 'Into T1', 5))
trd2 = Thread(target=write_file, args=('T2', r'files\t2_out.txt', 'Into T2', 3))

# Start the Thread
trd1.start()
trd2.start()

# Make the main program to wait until all the threads completing its execution
trd1.join()
trd2.join()

print('End of Main Program Execution')

print('-' * 75)
