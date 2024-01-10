import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        end_time = function()
        calc_time = end_time - start_time
        print(function.__name__ + " run speed: " + str(calc_time))
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
    return time.time()


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
    return time.time()


fast_function()
slow_function()
