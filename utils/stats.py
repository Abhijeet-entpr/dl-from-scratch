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
        breakpoint()
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

