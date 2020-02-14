import functools
import time
from tkinter import Event

from .console import PRINT, getPPrintStr




__all__ = ['debug', 'class_method_debug', 'check_time', 'debugTkinterEvent', 'pprint_debug']



def class_method_debug(cls: str or type, tag: str = '\n________________________________________________________________'):
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

            print(f"{tag} \n{cls}.{func.__name__}({signature})")
            result = func(*args, **kwargs)
            print(f"{func.__name__}  returned  {result!r}\n")  # 4

            return result
        return wrapper_debug
    return debug_inner



def debug(func: callable, tag: str = '\n________________________________________________________________'):
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

        print(f"{tag} \n{func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__}  returned  {result!r}\n")  # 4

        return result
    return wrapper_debug



def pprint_debug(func: callable, tag: str = '\n________________________________________________________________'):
    """
        Print the function signature and return value

    :param func: callable function to be debugged.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        signature = getPPrintStr({'args': kwargs, 'kwargs': args, })

        print(f"{tag} \n{func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__}  returned  {result!r}\n")

        return result
    return wrapper_debug



def check_time(*, cls: str or type = None, print_signature: bool = True, tag: str = '\n_______________________________check_time_______________________________'):
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



def debugTkinterEvent(func: callable, tag: str = '_______________________________TkinterEvent_______________________________'):
    @functools.wraps(func)
    def wrapper_debug(self, event: Event, *args, **kwargs):
        PRINT(f'{tag}\n{func.__class__}.{func.__name__}.{Event.__class__}', event.__dict__)

        result = func(self, event, *args, **kwargs)

        return result

    return wrapper_debug

