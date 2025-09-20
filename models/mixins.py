import time

class TimerMixin:
    """Mixin to measure execution time."""
    def time_execution(func):
        def wrapper(self, *args, **kwargs):
            start = time.time()
            result = func(self, *args, **kwargs)
            end = time.time()
            print(f"[{self.name}] Execution time: {end-start:.2f}s")
            return result
        return wrapper