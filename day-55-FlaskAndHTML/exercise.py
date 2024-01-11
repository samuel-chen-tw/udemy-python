# https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/7a66ccbe-1fc9-428d-bc99-6955e964ea88?sl=09fd55e5-7dfc-4b53-acaa-ed0674985806&st=8DflHAFj8zeeg2f1uWxMfL3GHC2IS4br
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
