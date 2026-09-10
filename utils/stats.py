import time
class RunningStats:

    def __init__(self):
        self._count = 0
        self._mean = 0.0
        self._M2 = 0.0

    def update(self, x: float)-> None:
        """Update running statistics with a new data sample.

        Parameters
        ----------
        x : float
         The new numeric sample to incorporate into the running stats.
        """
        #breakpoint()
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

import math

import math


def standardize(x: list[float]) -> list[float]:
    """Standardize a list of floats to zero mean and unit variance (Z-score)."""
    if not x:
        return []

    n = len(x)
    if n == 1:
        return [0.0]

    # 1. Calculate mean
    mean = sum(x) / n

    # 2. Calculate population variance & standard deviation (divide by n)
    variance = sum((val - mean) ** 2 for val in x) / n
    std_dev = math.sqrt(variance)

    # 3. Handle zero-variance edge case
    if std_dev == 0.0:
        return [0.0] * n

    # 4. Compute Z-scores
    return [(val - mean) / std_dev for val in x]