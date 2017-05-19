from __future__ import print_function
import time

COUNT = 100000000


def countdown(n):
    """ I am just a quick CPU bound method"""
    while n > 0:
        n -= 1
    return


def main():
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print('Time:', end - start)


if __name__ == '__main__':
    main()
