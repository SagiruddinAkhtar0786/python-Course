"""Function caching examples using Python."""

from functools import lru_cache
import time

# Example 1: Use built-in caching with functools.lru_cache
# This cache stores results of previous calls so repeated calls are fast.

@lru_cache(maxsize=None)
def expensive_factorial(n):
    if n == 0:
        return 1
    return n * expensive_factorial(n - 1)


# Example 2: Manual caching using a dictionary
# This is useful when you want to control cache behavior directly.

manual_cache = {}

def fib_cached(n):
    if n in manual_cache:
        return manual_cache[n]

    if n < 2:
        result = n
    else:
        result = fib_cached(n - 1) + fib_cached(n - 2)

    manual_cache[n] = result
    return result


if __name__ == "__main__":
    print("Function caching examples")

    # Measure lru_cache performance for factorial
    start = time.perf_counter()
    print("Factorial(20):", expensive_factorial(20))
    print("First factorial call took:", round(time.perf_counter() - start, 6), "seconds")

    start = time.perf_counter()
    print("Factorial(20) again:", expensive_factorial(20))
    print("Second factorial call took:", round(time.perf_counter() - start, 6), "seconds")

    print("Cached factorial function hits:", expensive_factorial.cache_info())
    print()

    # Measure manual cache performance for Fibonacci
    start = time.perf_counter()
    print("Fibonacci(30):", fib_cached(30))
    print("First fib_cached call took:", round(time.perf_counter() - start, 6), "seconds")

    start = time.perf_counter()
    print("Fibonacci(30) again:", fib_cached(30))
    print("Second fib_cached call took:", round(time.perf_counter() - start, 6), "seconds")
    print("Manual cache keys stored:", sorted(manual_cache.keys())[:10], "...")
