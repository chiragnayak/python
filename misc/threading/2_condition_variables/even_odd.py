import time
from threading import Thread, Condition, Lock


class PrintEvenOdd:
    count = 0
    cv = Condition()

    def print_even(self):
        while True:
            self.cv.acquire()
            if self.count % 2 == 0:
                print(f" Even : {self.count}")
                self.count += 1
                time.sleep(1)
                self.cv.notify_all()
                self.cv.release()
            else:
                self.cv.wait()

    def print_odd(self):
        while True:
            self.cv.acquire()
            if self.count % 2 != 0:
                print(f" Odd : {self.count}")
                self.count += 1
                time.sleep(1)
                self.cv.notify_all()
                self.cv.release()
            else:
                self.cv.wait()


class PrintEvenOdd_v2:
    count = 0
    cv = Condition()

    def print_even(self):
        while True:
            self.cv.acquire()
            if self.count % 2 == 0:
                print(f" Even : {self.count}")
                self.count += 1
                time.sleep(1)

            self.cv.release()

    def print_odd(self):
        while True:
            self.cv.acquire()
            if self.count % 2 != 0:
                print(f" Odd : {self.count}")
                self.count += 1
                time.sleep(1)

            self.cv.release()


class PrintEvenOdd_v3:
    count = 0
    lock = Lock()

    def print_even(self):
        while True:
            self.lock.acquire()
            if self.count % 2 == 0:
                print(f" Even : {self.count}")
                self.count += 1
                time.sleep(1)

            self.lock.release()

    def print_odd(self):
        while True:
            self.lock.acquire()
            if self.count % 2 != 0:
                print(f" Odd : {self.count}")
                self.count += 1
                time.sleep(1)

            self.lock.release()


if __name__ == "__main__":
    print_even_odd = PrintEvenOdd_v3()
    e_print = Thread(target=print_even_odd.print_even, args=())
    o_print = Thread(target=print_even_odd.print_odd, args=())

    o_print.start()
    e_print.start()
