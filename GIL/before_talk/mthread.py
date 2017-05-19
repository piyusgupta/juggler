from __future__ import print_function

import sys
import time
from threading import Thread

COUNT = 100000000


def countdown(n):
    """ I am just a quick CPU bound method"""
    while n > 0:
        n -= 1
    return


def main(thread_count):
    start = time.time()
    # create new threads and spawn it here
    for i in range(thread_count):
        t = Thread(target=countdown, args=(COUNT / thread_count,))
        t.start()
    # wait for all the threads to finish
    for i in range(thread_count):
        t.join()
    end = time.time()
    print('Time:', end - start)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE :: %s <int:thread_count>" % (__file__))
        sys.exit(0)
    main(int(sys.argv[1]))
