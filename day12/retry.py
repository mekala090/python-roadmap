import random
import time

def unreliable_task():
    if random.random() < 0.7:
        raise ConnectionError("Connection failed.")
    return "Success!"

def retry(func, max_attempts=5, delay=1):
    for attempt in range(1, max_attempts + 1):
        try:
            result = func()
        except ConnectionError as e:
            print(f"Attempt {attempt}/{max_attempts} failed: {e}")
            if attempt < max_attempts:
                time.sleep(delay)
        else:
            print(f"Attempt {attempt}: {result}")
            return result
    print("All attempts failed.")
    return None

retry(unreliable_task)