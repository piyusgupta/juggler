from __future__ import print_function

import sys
import time
import subprocess
import multiprocessing as mp

from threading import Thread

COUNT = 100000000


def countdown(n):
    """ I am just a quick CPU bound method"""
    while n > 0:
        n -= 1
    return


def main(thread_count):
    start = time.time()
    # create CPU - 1 processes to spin CPU uselessly
    processes = [subprocess.Popen(['python2.7', 'spin.py'])
                 for i in range(mp.cpu_count() - 1)]
    # create new threads and spawn it here
    for i in range(thread_count):
        t = Thread(target=countdown, args=(COUNT / thread_count,))
        t.start()
    # wait for all the threads to finish
    for i in range(thread_count):
        t.join()

    for p in processes:
        p.terminate()
    end = time.time()
    print('Time:', end - start)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE :: %s <int:thread_count>" % (__file__))
        sys.exit(0)
    main(int(sys.argv[1]))
