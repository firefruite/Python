"""
Asyncio is used to handle asynchronous processor and concurrent tasks

Demo of asyncio -- Asyncio using Asyncio.Task to execute three math function in parallel
"""

import asyncio
from utils import timer


@asyncio.coroutine
def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: Compute factorial(%s)" % (i))
        yield from asyncio.sleep(1)
        f *= i
    print("Asyncio.Task - factorial(%s) = %s" % (number, f))


@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: Compute fibonacci (%s)" % (i))
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))


@asyncio.coroutine
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
        print("Asyncio.Task: Compute binomialCoeff (%s)" % (i))
        yield from asyncio.sleep(1)
    print("Asyncio.Task - binomialCoeff(%s , %s) = %s" % (n, k, result))


@timer
def concurrency_with_task(loop):
    tasks = [asyncio.Task(factorial(10)),
             asyncio.Task(fibonacci(10)),
             asyncio.Task(binomialCoeff(20, 10))]
    loop.run_until_complete(asyncio.wait(tasks))


@timer
def concurrency_with_gather(loop):
    tasks = [asyncio.Task(factorial(10)),
             asyncio.Task(fibonacci(10)),
             asyncio.Task(binomialCoeff(20, 10))]
    loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    concurrency_with_task(loop)
    concurrency_with_gather(loop)
