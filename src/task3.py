from time import time
from contextlib import redirect_stdout
import inspect
import io
from datetime import datetime

# TODO: Add an clear desciton
class Decorator_1:
    def __init__(self, function):
        self.function = function
        self.call_counter = 0

    def __call__(self, *args, **kwargs):
        self.call_counter += 1
        st = time()
        with redirect_stdout(io.StringIO()) as f:
            result = self.function(*args, **kwargs)
            fun_result = f.getvalue()
        print(
            f"{self.function.__name__} call {self.call_counter} executed in {time() - st : 0.4f} sec"
        )
        return result

# TODO: Add an clear desciton
class Decorator_2:
    function_run_times = {}

    def __init__(self, function):
        self.function = function
        self.call_counter = 0

    def __call__(self, *args, **kwargs):
        with redirect_stdout(open("Decorator3_out.txt", "a")):
            self.call_counter += 1
            st = time()
            fun_result = ""
            result = 0
            with redirect_stdout(io.StringIO()) as f:
                try:
                    result = self.function(*args, **kwargs)
                    fun_result = f.getvalue()
                except Exception as e:
                    with open("Error log.txt", "a") as f:
                        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                        f.write("\t" + str(e) + "\n")
            run_time = time() - st
            Decorator_2.function_run_times[self.function.__name__] = run_time

            print(
                f"{self.function.__name__} call {self.call_counter} executed in {run_time : 0.4f} sec"
            )
            print(f"Name:   {self.function.__name__}")
            print(f"Type:   {type(self.function)}")
            print(f"Sign:   {inspect.signature(self.function)}")
            print(
                f"Args:   positional {args}\n{' '*8}key=worded {kwargs}", end="\n\n")

            print("Doc:".ljust(8), end="")

            if self.function.__doc__ is not None:
                print(
                    inspect.getdoc(self.function).replace(
                        "\n", "\n" + " " * 8),
                    end="\n\n",
                )
            else:
                print()
            print("Source: ", end="")
            print(
                inspect.getsource(self.function).replace("\n", "\n" + " " * 8),
                end="\n\n",
            )

            print("Output: ", end="")
            print(fun_result.replace("\n", "\n" + " " * 8), end="\n\n")

        return result


if __name__ == "__main__":

    @Decorator_2
    def funh(bar1, bar2=""):
        """
        This function does something useful
        :param bar1: description
        :param bar2: description
        """
        print("some\nmultiline\noutput")

    funh(None, bar2="")
