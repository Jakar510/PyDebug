import functools


__all__ = ['debug']

def debug(func: callable, tag: str = '__debug__'):
    """
        Print the function signature and return value

    :param func: callable function to be debugged.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"\n{tag}.Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}\n")  # 4
        return value
    return wrapper_debug
