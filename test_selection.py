import time
import random
from deterministic_selection import deterministic_select
from randomized_selection import quickselect

# Generate test data
sizes = [1000, 5000, 10000, 50000, 100000]
for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    k = size // 2  # Median

    # Test deterministic selection
    start = time.time()
    median_deterministic = deterministic_select(arr[:], k)
    end = time.time()
    print(f"Deterministic Selection ({size} elements): {end - start:.6f} seconds")

    # Test randomized selection
    start = time.time()
    median_randomized = quickselect(arr[:], k)
    end = time.time()
    print(f"Randomized Selection ({size} elements): {end - start:.6f} seconds")
    print("-" * 50)
