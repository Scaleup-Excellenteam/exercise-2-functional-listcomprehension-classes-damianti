import functools


class TypeCheckError(TypeError):
    """
    Custom error class for type checking.
    Inherits from the built-in TypeError class.
    Raised when the argument type does not match the expected type.
    """

    def __init__(self, expected_type, received_type):
        super().__init__(f"Expected type {expected_type}, but received type {received_type}")


def type_check(correct_type):
    """
    Decorator factory for type checking.
    Takes the expected type as an argument and returns a decorator.

    :param correct_type: The expected type of the argument of the decorated function.
    :return: A decorator function that checks the type of the first argument.
    """

    def decorator(func):
        """
        Decorator for type checking.
        Wraps the given function with a wrapper function that checks the type of the first argument.

        :param func: The function to be decorated.
        :return: The wrapped function with type checking.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function for type checking.
            Checks if the first argument is of the correct type, raises a TypeCheckError if not.

            :param args: Positional arguments passed to the wrapped function.
            :param kwargs: Keyword arguments passed to the wrapped function.
            :return: The result of calling the wrapped function with the given arguments.
            """

            if len(args) == 0 or not isinstance(args[0], correct_type):
                raise TypeCheckError(correct_type, type(args[0]))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    """
    Multiplies the given number by 2.

    :param num: The number to be multiplied.
    :return: The result of multiplying the number by 2.
    """
    return num * 2


# Test cases
print(times2(4))  # Should output 8

try:
    print(times2('4'))  # Should raise TypeCheckError
except TypeCheckError as e:
    print(e)  # Output: Expected type <class 'int'>, but received type <class 'str'>
