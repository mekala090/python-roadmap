import functools
import time


def program_6_decorator_with_arguments():
    print("\n=== Program 6: Decorator with arguments ===")
 
    def repeat(times):
        """Run the decorated function `times` times."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
 
    @repeat(times=3)
    def say_hi(name):
        print(f"Hi, {name}!")
 
    say_hi("Asha")
 
    # A more practical example: retry on failure
    def retry(max_attempts=3, delay=0.1):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"attempt {attempt} failed: {e}")
                        if attempt == max_attempts:
                            raise
                        time.sleep(delay)
            return wrapper
        return decorator
 
    state = {"n": 0}
 
    @retry(max_attempts=4, delay=0.05)
    def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise ConnectionError("network down")
        return "success"
 
    print("result:", flaky())
 
 
if __name__ == "__main__":
    program_6_decorator_with_arguments()
 