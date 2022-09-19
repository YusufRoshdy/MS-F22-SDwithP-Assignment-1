from time import time
from contextlib import redirect_stdout
import inspect
import io


def decorator_2(function):
    def wrapper(*args, **kwargs):
        wrapper.call_counter += 1
        st = time()
        with redirect_stdout(io.StringIO()) as f:
            result = function(*args, **kwargs)
        print(f"{function.__name__} call {wrapper.call_counter} executed in {time() - st : 0.4f} sec")
        print(f"Name:   {function.__name__}")
        print(f"Type:   {type(function)}")
        print(f"Sign:   {inspect.signature(function)}")
        print(f"Args:   positional {args}\n{' '*8}key=worded {kwargs}", end="\n\n")

        print("Doc:".ljust(8), end="")

        if function.__doc__ is not None:
            print(inspect.getdoc(function).replace("\n", "\n" + " " * 8), end="\n\n")
        else:
            print()
        print("Source: ", end="")
        print(inspect.getsource(function).replace("\n", "\n" + " " * 8), end="\n\n")

        print("Output: ", end="")
        print(f.getvalue().replace("\n", "\n" + " " * 8), end="\n\n")

        return result

    wrapper.call_counter = 0
    return wrapper


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


if __name__ == "__main__":
    funh(None, bar2="")
