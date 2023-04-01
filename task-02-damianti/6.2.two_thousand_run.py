
import time


def timer(f, *args, **kwargs):
    """The timer function takes the following parameters:

    :param f: the function to be measured
    :param args: any positional arguments that f requires
    :param kwargs: any keyword arguments that f requires
    :return: the execution time of the function as a floating-point number.
    """
    start = time.time()

    f(*args, **kwargs)

    end = time.time()
    return end - start


if __name__ == "__main__":
    # measure the execution time of the print function
    time_spent = timer(print, "Hello")
    print(f'Time taken: {time_spent:.10f} seconds')

    # measure the execution time of the zip function
    time_spent = timer(zip, [1, 2, 3], [4, 5, 6])
    print(f'Time taken: {time_spent:.10f} seconds')

    # measure the execution time of the format method of a string
    time_spent = timer("Hi {name}".format, name="Bug")
    print(f'Time taken: {time_spent:.10f} seconds')
