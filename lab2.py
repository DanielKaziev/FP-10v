import timeit

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

execution_time = timeit.timeit(lambda: fibonacci(400), number=1)
print(f"Время выполнения 1: {execution_time} секунд")

execution = timeit.timeit(lambda: fibonacci(400), number=10)
print(f"Время выполнения 2: {execution} секунд")
