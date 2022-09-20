import random
from math import sqrt

from task1 import decorator_1
from task2 import decorator_2
from task3 import Decorator_1, Decorator_2

test_decorator = Decorator_2


@test_decorator
def cube(n=10):
    """This is a dummy function that return n*n*n"""
    _cube = lambda x: x ** 3
    n_cube = _cube(n)
    for i in range(n):
        print(i * i * i)
    return n_cube


@test_decorator
def sum_sqr(my_list=[10]):
    """This is a dummy function that return sum(x**2)"""
    _sqr = lambda x: x ** 2
    my_sum = sum([_sqr(x) for x in my_list])
    print(my_sum)
    return my_sum


@test_decorator
def pascal(n=10):
    next_element = lambda x: x * (i - j) // j
    for i in range(1, n + 1):
        C = 1
        for j in range(1, i + 1):
            print(C, end=" ")
            C = next_element(C)
        print()


@test_decorator
def quadratic(a=1, b=1, c=1):
    # https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/
    # function for finding roots
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

    # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(-b / (2 * a), " + i", sqrt_val)
        print(-b / (2 * a), " - i", sqrt_val)

@test_decorator
def error_fun():
    return 5/0


if __name__ == "__main__":
    print("Task 3 and 4")
    cube(1000)

    sum_sqr([x for x in range(100)])

    pascal()

    quadratic()

    error_fun()

    ranking = sorted(
        Decorator_2.function_run_times,
        key=lambda x: Decorator_2.function_run_times[x],
    )
    print("PROGRAM  | RANK | TIME ELAPSED")
    for i in range(len(ranking)):
        fun_name = ranking[i]
        print(
            f"{fun_name: <9}{i+1 : 6}     {Decorator_2.function_run_times[fun_name] : 8.5f}s"
        )
