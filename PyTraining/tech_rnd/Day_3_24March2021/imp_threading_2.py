print('-' * 75)

from threading import Thread, Lock
from time import sleep
from datetime import datetime

class ImplementThread(Thread):
    all_trds = []
    trdLock = Lock()

    def __init__(self, trd_name, fname, msg, delay):
        # Call to super init method
        super().__init__()           # Thread.__init__(self)

        self.trd_name = trd_name
        self.fname = fname
        self.msg = msg
        self.delay = delay

        # TEA BREAK - BACK @ 04:50PM

        # Add the thread to all threads
        ImplementThread.all_trds.append(self)

    def write_file(self):
        with open(self.fname, 'w') as fwrite:
            for n in range(1, 6):
                tstamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                fwrite.write(f'{tstamp} => {self.msg}\n')
                sleep(self.delay)

    def run(self):
        # Acquire the Lock
        ImplementThread.trdLock.acquire()

        print(f'{self.trd_name} Started')
        self.write_file()
        print(f'{self.trd_name} Ended')

        # Release the Lock
        ImplementThread.trdLock.release()

# Create the threaded objects for our custom thread class
trd1 = ImplementThread('T1', r'files\t1_out.txt', 'Into T1', 5)
trd2 = ImplementThread('T2', r'files\t2_out.txt', 'Into T2', 3)

print('All Threads -', ImplementThread.all_trds)

# Start the threads
for trd in ImplementThread.all_trds:
    trd.start()

# Make the main program to wait until all the threads completes its execution
for trd in ImplementThread.all_trds:
    trd.join()

print('End of Main Program Execution')

print('-' * 75)
