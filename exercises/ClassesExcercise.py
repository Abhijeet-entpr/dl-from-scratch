import time


class RunningStats:

    def __init__(self):
        self._count = 0
        self._mean = 0.0
        self._M2 = 0.0

    def update(self, x: float)-> None:
        self._count += 1
        delta = x - self._mean
        self._mean += delta / self._count
        delta2 = x - self._mean
        self._M2 += delta * delta2

    @property
    def count(self) -> int:
        return self._count

    @property
    def mean(self) -> float:
        return self._mean

    @property
    def var(self) -> float:
        return self._M2 / (self._count - 1) if self._count > 1 else 0.0

    def __repr__(self) -> str:
        return f"RunningStats(count={self.count}, mean={self.mean:.4f}, var={self.var:.4f})"

obj = RunningStats()
obj.update(1.0)
obj.update(2.0)
obj.update(3.0)
print(obj)


class Timer:

    def __init__(self):
        self.elapsed_time = 0.0
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        self.elapsed_time = end_time - self.start_time


# Usage with 'with' block context manager:
with Timer() as t:
    for _ in range(10000000):
        pass

print(f"Elapsed time: {t.elapsed_time:.6f} seconds")


# VERIFICATION ASSERTIONS
# ==========================================================

if __name__ == "__main__":
    data = [2, 2, 2, 4, 4, 5, 5, 7, 9, 9]
    stats = RunningStats()
    for x in data:
        stats.update(x)

    # 1. Count assertion
    assert stats.count == 10, f"Expected count 10, got {stats.count}"

    # 2. Mean assertion (Expected: 4.9)
    assert abs(stats.mean - 4.9) < 1e-9, f"Expected mean 4.9, got {stats.mean}"

    # 3. Sample Variance assertion (Expected: 64.9 / 9 ≈ 7.2111111)
    expected_var = 64.9 / 9
    assert (
        abs(stats.var - expected_var) < 1e-6
    ), f"Expected var {expected_var}, got {stats.var}"

    # 4. Timer Context Manager assertion
    with Timer() as t:
        time.sleep(0.01)

    assert t.elapsed_time >= 0.01, f"Timer failed: elapsed {t.elapsed}s"

    print("All 4 assertions passed successfully!")
    print(stats)