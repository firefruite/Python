"""
Show how to create threads

All status of thread: ready, run, blocking

The steps of implementing a thread:
    1. create a subclass of threading.Thread
    2. overwrite __init__()
    3. overwrite run()
"""

import threading
from time import sleep


def func(i):
    sleep(1)
    print("function called by %s %d\n" % (threading.current_thread().name, i))


if __name__ == '__main__':
    threads = []

    for i in range(5):
        # Thread(group, target, name, args=(), kwargs={})
        # name: the unique name of thread
        t = threading.Thread(target=func, args=(i,))
        threads.append(t)
        t.start()  # start the thread --> activity

    # for i in range(5):
    #     t = threads[i]
    #     t.join()  # wait until the thread over
