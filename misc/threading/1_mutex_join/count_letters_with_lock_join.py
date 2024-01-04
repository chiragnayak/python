import json
import threading
from threading import Lock
from urllib import request
import time


def count_letters_from_url(url, frequency, mutex):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    url_response = request.urlopen(req)
    data = str(url_response.read())
    mutex.acquire()
    for l in data:
        c = l.lower()
        if c in frequency:

            frequency[c] = frequency[c] + 1

    print(f"Processed {url}...")
    mutex.release()


if __name__ == "__main__":

    letters = "abcdefghijklmnopqrstuvwzyz"

    mutex = Lock()

    frequency_map = {}
    for l in letters:
        frequency_map[l] = 0

    url = "https://www.rfc-editor.org/rfc/rfc"

    start = time.time()
    threads = list()
    for _ in range(1000, 1020):
        url_string = f"{url}{_}"
        thread = threading.Thread(target=count_letters_from_url(url_string, frequency_map, mutex))
        threads.append(thread)
        thread.start()

    for t in threads:
            t.join()

    end = time.time()

    print(json.dumps(frequency_map, indent=4))
    print(f"It took {end-start} seconds...")