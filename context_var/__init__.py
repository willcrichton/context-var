from contextlib import contextmanager


class ContextVar:
    """
    Dynamically-scoped "context" variable.

    See tests/test_all.py for example usage.
    """
    def __init__(self, default=None):
        self.values = [default]

    @contextmanager
    def set(self, value):
        self.values.append(value)
        yield
        self.values.pop()

    def get(self):
        return self.values[-1]
