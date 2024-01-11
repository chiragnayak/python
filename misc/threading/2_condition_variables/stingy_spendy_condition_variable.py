import time
from threading import Thread, Condition

"""
condition variable

acquire() --> acquires the lock
release() --> releases he lock
wait() --> releases the lock automatically
notify() --> notifies single thread
notifyAll() --> notifies all threads

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
