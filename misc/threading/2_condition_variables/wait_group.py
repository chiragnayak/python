"""
wait group:

there will be multiple threads in a wait group until all are done we should wait.
just using join will required to have to put join on each thread explicitely. What if one thread spawns
another thread.
implement a wait_group, which has below functionality

count --> current active threads
wait() --> wait if any threads are in running state
add(x) --> add more threads to the group
done() --> called when a thread in group is done/finished

"""

from threading import Thread, Condition


class WaitGroup:
    wait_count = 0
    cv = Condition()

    def add(self, count):
        self.cv.acquire()
        self.wait_count += count
        print(f"(add) Count : {self.wait_count}")
        self.cv.release()

    def done(self):
        self.cv.acquire()
        if self.wait_count > 0:
            self.wait_count -= 1

        print(f"(done) Count : {self.wait_count}")

        # check if the count is zero, i.e. all execution complete then notify all
        if self.wait_count == 0:
            print(f"(done) Count : {self.wait_count}.. Notify All")
            self.cv.notify_all()
        self.cv.release()

    def wait(self):
        self.cv.acquire()
        while self.wait_count > 0:
            print(f"(wait) Count : {self.wait_count}")
            self.cv.wait()
        self.cv.release()
