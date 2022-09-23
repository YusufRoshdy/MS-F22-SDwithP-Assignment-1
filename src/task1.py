from time import time
from contextlib import redirect_stdout
import io


def decorator_1(function):
    def wrapper(*args, **kwargs):
        wrapper.call_counter += 1
        st = time()
        with redirect_stdout(io.StringIO()) as f:
            result = function(*args, **kwargs)
            fun_result = f.getvalue()   # This variable is not accessed
        print(
            f"{function.__name__} call {wrapper.call_counter} executed in {time() - st : 0.4f} sec"
        )
        return result

    wrapper.call_counter = 0
    return wrapper


if __name__ == "__main__":
    import random
    from math import sqrt

    @decorator_1
    def func():
        # print("I am ready to Start")
        result = 0
        n = random.randint(10, 1751)
        for i in range(n):
            result += i ** 2

    @decorator_1
    def funx(n=2, m=5):
        print("I am ready to do serious stuff")
        max_val = float("-inf")
        n = random.randint(10, 1751)
        res = [pow(i, 2) for i in range(n)]
        for i in res:
            if i > max_val:
                max_val = i

    func()
    funx()
    func()
    funx()
    func()
