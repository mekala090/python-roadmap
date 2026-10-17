import functools
import time


def program_4_call_counter():
    print("\n=== Program 4: Decorator that counts calls ===")
 
    def count_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            print(f"{func.__name__} called {wrapper.calls} time(s)")
            return func(*args, **kwargs)
        wrapper.calls = 0        # function objects can hold attributes
        return wrapper
 
    @count_calls
    def greet(name):
        return f"Hello, {name}!"
 
    print(greet("Asha"))
    print(greet("Ravi"))
    print(greet("Meera"))
    print("Total calls:", greet.calls)
 
 
def program_5_timing_and_logging():
    print("\n=== Program 5: Timing and logging decorators ===")
 
    def timer(func):
        """Print how long the function takes to run."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"[timer] {func.__name__} took {elapsed:.6f}s")
            return result
        return wrapper
 
    def logger(func):
        """Log the arguments and the return value."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[log] calling {func.__name__} args={args} kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[log] {func.__name__} returned {result!r}")
            return result
        return wrapper
 
    # Decorators stack: applied bottom-up (logger first, then timer)
    @timer
    @logger
    def sum_squares(n):
        return sum(i * i for i in range(n))
 
    sum_squares(1_000_000)


if __name__ == "__main__":
    program_4_call_counter()
    program_5_timing_and_logging()
 