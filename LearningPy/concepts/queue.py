def do_work(item):
    print("Processing !! --> {} by --> {} ".format(item, threading.current_thread().name))
    sleep(1)


def worker():
    while True:
        # get processing item from queue when available
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()


def source():
    return [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    num_worker_threads = 3

    q = queue.Queue()
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for item in source():
        q.put(item)
        sleep(1)
        print("{} added".format(item))

    # block until all tasks are done
    q.join()

    # stop workers
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()
