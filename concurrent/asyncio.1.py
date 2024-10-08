"""
Demo of asyncio
1. call_later(delay, callback, args) -- after delay, calling the callback
2. call_soon(callback, args) -- to call the callback as soon as
3. time() -- return time in float
4. set_event_loop() -- set event for current context
5. new_event_loop() -- create a new event
6. run_forever() -- run until calling stop() function
7. get_event_loop() -- get the event in current context
"""

import asyncio


def function_1(end_time, loop):
    print("function_1 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()


def function_2(end_time, loop):
    print("function_2 called ")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_3, end_time, loop)
    else:
        loop.stop()


def function_3(end_time, loop):
    print("function_3 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()


def function_4(end_time, loop):
    print("function_4 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_4, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

end_loop = loop.time() + 9.0
loop.call_soon(function_1, end_loop, loop)
# loop.call_soon(function_4, end_loop, loop)
loop.run_forever()
loop.close()
