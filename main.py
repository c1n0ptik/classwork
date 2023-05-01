import time


def calc(func):
    def wrapper(n):
        start_time = time.perf_counter()
        func(n)
        end_time = time.perf_counter()
        return f"The execution time: {end_time - start_time:.8f} seconds"

    return wrapper


@calc
def fibonacci(n):
    if n < 2:
        return n
    time.sleep(1)
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))
