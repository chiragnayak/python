import time
from threading import Thread, Condition

"""
condition variable

acquire() --> acquires the lock
release() --> releases the lock
wait() --> releases the lock automatically
notify() --> notifies single thread
notifyAll() --> notifies all threads

Note: The wait() method releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all().
 Once awakened, wait() re-acquires the lock and returns. It is also possible to specify a timeout.

Note: the notify() and notify_all() methods don’t release the lock; 
this means that the thread or threads awakened will not return from their wait() call immediately, 
but only when the thread that called notify() or notify_all() finally relinquishes ownership of the lock

producer-consumer situation with unlimited buffer capacity:

# Consume one item
with cv:
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()

# Produce one item
with cv:
    make_an_item_available()
    cv.notify()

"""

class StingySpendy:
    money = 100
    cv = Condition()

    def stingy(self):
        for i in range(1, 1000000):
            self.cv.acquire()
            # print("Saving ..")
            self.money += 10
            self.cv.notify()
            self.cv.release()

        print("Stingy Done")

    def spendy(self):
        for i in range(1, 500000):
            self.cv.acquire()
            while self.money < 20:
                print(f"Money is zero/less before spending !! {self.money}")
                self.cv.wait()
            # print("Spending ..")
            self.money -= 20
            if self.money < 0:
                print(f"Money in back is less than zero : {self.money}")
            self.cv.release()

        print("Spendy Done")


if __name__ == "__main__":
    ss = StingySpendy()
    t_stingy = Thread(target=ss.stingy(), args=())
    t_spendy = Thread(target=ss.spendy(), args=())

    t_stingy.start()
    t_spendy.start()

    time.sleep(5)

    print(f"Money at the end {ss.money}")
