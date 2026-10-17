class Countdown:
    """Iterator that counts down from `start` to 1."""
 
    def __init__(self, start):
        self.current = start
 
    def __iter__(self):
        return self              # the object is its own iterator
 
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # tells the for-loop to stop
        value = self.current
        self.current -= 1
        return value
 
 
def program_1_iterator():
    print("=== Program 1: Custom iterator (Countdown) ===")
    for n in Countdown(5):
        print(n, end=" ")
    print()
 
    # What a for-loop does behind the scenes:
    it = iter(Countdown(3))
    print(next(it), next(it), next(it))
    try:
        next(it)
    except StopIteration:
        print("StopIteration raised: iterator exhausted")


if __name__ == "__main__":
   program_1_iterator()