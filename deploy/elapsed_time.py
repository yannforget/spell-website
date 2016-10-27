#!/usr/bin/env python3

import sys
from datetime import datetime, timedelta


def main(logfile):
    """Returns elpased time in seconds since
    the last run of the script.
    """
    with open(logfile, 'r') as log:
        lastrun = log.read().replace('\n', '')
        lastrun = datetime.strptime(lastrun, '%m/%d/%Y %H:%M:%S')
    print((datetime.now() - lastrun).seconds)

if __name__ == '__main__':
    main(sys.argv[1])
