from functools import lru_cache


@lru_cache()
def fib(num):
    return 1 if num in (1, 2) else fib(num - 1) + fib(num - 2)


for num in range(1, 101):
    print(f'{num}: {fib(num)}')
