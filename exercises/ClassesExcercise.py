import time


# class RunningStats:

#     def __init__(self):
#         self._count = 0
#         self._mean = 0.0
#         self._M2 = 0.0

#     def update(self, x: float)-> None:
#         self._count += 1
#         delta = x - self._mean
#         self._mean += delta / self._count
#         delta2 = x - self._mean
#         self._M2 += delta * delta2

#     @property
#     def count(self) -> int:
#         return self._count

#     @property
#     def mean(self) -> float:
#         return self._mean

#     @property
#     def var(self) -> float:
#         return self._M2 / (self._count - 1) if self._count > 1 else 0.0

#     def __repr__(self) -> str:
#         return f"RunningStats(count={self.count}, mean={self.mean:.4f}, var={self.var:.4f})"

# obj = RunningStats()
# obj.update(1.0)
# obj.update(2.0)
# obj.update(3.0)
# print(obj)


class Timer:
    def __init__(self):
        self.elapsed_time = 0.0
        self.start_time = 0.0

    def enter(self):
        self.start_time = time.perf_counter()
        return self

    def exit(self):
        end_time = time.perf_counter()
        self.elapsed_time = end_time - self.start_time
        return self.elapsed_time

timer = Timer()
timer.enter()
# Simulate some code execution
for _ in range(100000000):
    pass
elapsed = timer.exit()
print(f"Elapsed time: {elapsed:.6f} seconds")
