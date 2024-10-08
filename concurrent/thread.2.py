"""
Use queue to manage the shared resource

The common functions:
    1. put() -- adding an item
    2. get() -- getting an item
    3. task_done() -- calling it when an item was done
    4. join() -- wait until all item done
"""

from threading import Thread, Event
from queue import Queue
import time
import random


class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify: item %d appended to queue by %s' % (item, self.name))
            time.sleep(1)


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify : %d popped from queue by %s' % (item, self.name))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
