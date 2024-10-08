"""
Demo of concurrent futures
    1. thread pool
    2. processor pool
"""
import timeit
import time
import concurrent.futures


def sync_exec():
    number_list = list(range(1, 11))
    for i in number_list:
        i *= count()


def async_exec_with_thread_pool():
    number_list = list(range(1, 11))

    def async_exec(i):
        i *= count()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(async_exec, i) for i in number_list]


def async_exec_with_process_pool():
    number_list = list(range(1, 11))

    def async_exec(i):
        i *= count()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(async_exec, i) for i in number_list]


def count():
    """
    Simulating CPU intensive task
    :return:
    """
    num = 0
    for i in range(1, 10000001):
        num += i
    return num


if __name__ == '__main__':
    # sync order --> 6.824370100002852
    it = timeit.timeit('sync_exec()', setup='from __main__ import sync_exec', number=1)
    print(it)

    # thread pool --> 7.901989899997716
    # GIL --> Only authorize a thread to use cpu every time
    it = timeit.timeit('async_exec_with_thread_pool()', setup='from __main__ import async_exec_with_thread_pool', number=1)
    print(it)

    # thread pool --> 0.27624459999788087
    it = timeit.timeit('async_exec_with_process_pool()', setup='from __main__ import async_exec_with_process_pool', number=1)
    print(it)
