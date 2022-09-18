from time import time, sleep
from contextlib import redirect_stdout
import io


def decorator_1(function):
    def wrapper(*args, **kwargs):
        wrapper.call_counter += 1
        st = time()
        with redirect_stdout(io.StringIO()) as f:
            result = function(*args, **kwargs)
        print(
            f"{function.__name__} call {wrapper.call_counter} executed in {time() - st : 0.4f} sec"
        )
        return result

    wrapper.call_counter = 0
    return wrapper
