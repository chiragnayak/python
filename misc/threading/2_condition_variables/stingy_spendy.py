import time
from threading import Thread, Lock


class StingySpendy:
    money = 0
    mutex = Lock()

    def stingy(self):
        for i in range(1, 100):
            self.mutex.acquire()
            print("Saving ..")
            self.money += 10
            self.mutex.release()

        print("Stingy Done")

    def spendy(self):
        for i in range(1, 100):
            self.mutex.acquire()
            print("Spending ..")
            if self.money <= 0:
                print(f"Money is zero/less before spending !! {self.money}")
            self.money -= 20
            self.mutex.release()

        print("Spendy Done")


if __name__ == "__main__":
    ss = StingySpendy()
    t_stingy = Thread(target=ss.stingy(), args=())
    t_spendy = Thread(target=ss.spendy(), args=())

    t_stingy.start()
    t_spendy.start()

    time.sleep(5)

    print(f"Money at the end {ss.money}")
