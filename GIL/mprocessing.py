"""
Multiprocessing version of the serial.py which
create subprocess for the task to complete.
"""
from __future__ import print_function

import sys
import multiprocessing as mp

from logger import logger

COUNT = 10000000


def countdown(n):
    """ I am just a quick CPU bound method"""
    while n > 0:
        n -= 1
    return


@logger
def main(process_count):
    # create multiple processes
    processes = [mp.Process(target=countdown, args=(COUNT / process_count,))
                 for p in range(process_count)]
    # start running them
    for proc in processes:
        proc.start()
    # Exits the completed process
    for proc in processes:
        proc.join()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE :: %s <int:process_count>" % (__file__))
        sys.exit(0)
    main(int(sys.argv[1]))
