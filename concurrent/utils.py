import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        execution_time = end - start
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        return result

    return wrapper