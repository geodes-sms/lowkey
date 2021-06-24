#!/usr/bin/env python
import threading
import time

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


def main():
    thread1 = threading.Thread(target=network, args=())
    thread1.daemon = True
    print("Starting network thread")
    thread1.start()
    print("Starting editor thread")
    editor()

def network():
    while True:
        print("network")
        time.sleep(0.5)

def editor():
    while True:
        print("editor")
        time.sleep(1)

if __name__ == '__main__':
    main()