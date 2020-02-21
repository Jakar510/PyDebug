import functools
import time
from tkinter import Event

from .console import PRINT, getPPrintStr




__all__ = ['debug', 'class_method_debug', 'check_time', 'debugTkinterEvent', 'pprint_debug']

DEFAULT_TAG = '\n_______________________________  "{0}"  _______________________________'

def class_method_debug(cls: str or type, tag: str = DEFAULT_TAG):
    """
        Print the function signature and return value

    :param cls: class string or type to describe the method's parent or caller.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    if isinstance(cls, type):
        cls = cls.__name__

    def debug_inner(func: callable = None):
        """
            Print the function signature and return value

        :param func: callable function to be debugged.
        :return:
        """
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            try: args_repr = [repr(a) for a in args]  # 1
            except: args_repr = [str(a) for a in args]  # 1

            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2

            signature = ", ".join(args_repr + kwargs_repr)  # 3

            print(f"{tag.format(f'{func.__module__}.{func.__qualname__}')} \n{cls}.{func.__name__}(\n{signature}\n)")
            result = func(*args, **kwargs)
            print(f"{func.__name__}  returned  {result!r}\n")  # 4

            return result
        return wrapper_debug
    return debug_inner



def debug(func: callable, tag: str = DEFAULT_TAG):
    """
        Print the function signature and return value

    :param func: callable function to be debugged.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        try: args_repr = [repr(a) for a in args]  # 1
        except: args_repr = [str(a) for a in args]  # 1

        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2

        signature = ", ".join(args_repr + kwargs_repr)  # 3

        print(f"{tag.format(f'{func.__module__}.{func.__qualname__}')} \n{func.__qualname__}(\n{signature}\n)")
        result = func(*args, **kwargs)
        print(f"{func.__name__}  returned  {result!r}\n")  # 4

        return result
    return wrapper_debug



def pprint_debug(func: callable, tag: str = DEFAULT_TAG):
    """
        Print the function signature and return value

    :param func: callable function to be debugged.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        signature = getPPrintStr({'kwargs': kwargs, 'args': args, })
        print(f"{tag.format(f'{func.__module__}.{func.__qualname__}')} \n{func.__qualname__}(\n{signature}\n)")
        result = func(*args, **kwargs)
        print(f"{func.__name__}  returned  {result!r}\n")

        return result
    return wrapper_debug



def check_time(*, cls: str or type = None, print_signature: bool = True, tag: str = DEFAULT_TAG):
    """
        Print the function signature and return value

    :param print_signature:
    :param cls: class string or type to describe the method's parent or caller.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    if isinstance(cls, type):
        cls = cls.__name__

    def timeit(func: callable):
        @functools.wraps(func)
        def timed(*args, **kwargs):
            print(tag)
            if print_signature:
                try: args_repr = [repr(a) for a in args]  # 1
                except: args_repr = [str(a) for a in args]  # 1

                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2

                signature = ", ".join(args_repr + kwargs_repr)  # 3

                if cls is not None:
                    print(f"\n{cls}.{func.__name__}\n{signature}")
                else:
                    print(f"\n{func.__name__}\n{signature}")

            start_time = time.time()
            result = func(*args, **kwargs)
            print(f'{func.__name__}  took  {time.time() - start_time}')
            print(f"{func.__name__}  returned  {result!r}\n")  # 4
            return result

        return timed
    return timeit



def debugTkinterEvent(func: callable, tag: str = DEFAULT_TAG):
    @functools.wraps(func)
    def wrapper_debug(self, event: Event, *args, **kwargs):
        PRINT(f'{tag.format("TkinterEvent")}\n{func.__class__}.{func.__name__}.{Event.__class__}', event.__dict__)

        result = func(self, event, *args, **kwargs)

        return result

    return wrapper_debug

