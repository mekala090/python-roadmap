def program_2_fibonacci():
    print("\n=== Program 2: Fibonacci generator ===")
 
    def fibonacci(limit):
        """Yield the first `limit` Fibonacci numbers."""
        a, b = 0, 1
        for _ in range(limit):
            yield a
            a, b = b, a + b
 
    print(list(fibonacci(10)))
 
    # Infinite version: safe because values are produced lazily
    def fibonacci_forever():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
 
    gen = fibonacci_forever()
    print([next(gen) for _ in range(8)])
 
 
def program_3_read_large_file():
    print("\n=== Program 3: Generator to read a large file ===")
 
    def read_lines(path):
        """Yield one line at a time; the whole file is never in memory."""
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                yield line.rstrip("\n")
 
    def read_in_chunks(path, chunk_size=1024):
        """Yield fixed-size chunks (useful for binary/huge files)."""
        with open(path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk


if __name__ == "__main__":
    program_2_fibonacci()
 