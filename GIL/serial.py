"""
This is a serial program execution test
It will do the countdown for 10M numbers
in serial fashion as single thread does in python.
"""
from logger import logger


def countdown(n):
    """ I am just a quick CPU bound method"""
    while n > 0:
        n -= 1
    return


COUNT = 10000000


@logger
def main():
    countdown(COUNT)


if __name__ == '__main__':
    main()
