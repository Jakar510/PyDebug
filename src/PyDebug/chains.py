import functools
from .base import GetFunctionName, DEFAULT_TAG

from .console import getPPrintStr




__all__ = ['top_debug', 'sub_level', ]

def print_chain_signature(func: callable, tag: str, level: int or str, signature: bool, *args, **kwargs):
    assert ('{0}' in tag)
    name = GetFunctionName(func)
    print(tag.format(f'{level}'))

    if signature and (args or kwargs):
        signature = getPPrintStr({ 'kwargs': kwargs, 'args': args, })
        print(f"{name}(\n      {signature}\n   )")
        result = func(*args, **kwargs)
        print(f"{name}  returned: \n{getPPrintStr(result)}\n")

def top_debug(func: callable, tag: str = DEFAULT_TAG):
    """
        Print the function signature and return value

    :param func: callable function to be debugged.
    :param tag: a unique string to identify the output in the console window.
    :return:
    """
    name = GetFunctionName(func)

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        print(tag.format(name))
        signature = getPPrintStr({ 'kwargs': kwargs, 'args': args, })
        print(f"{name}(\n      {signature}\n   )")
        result = func(*args, **kwargs)
        print(f"{name}  returned: \n{getPPrintStr(result)}\n")

        return result
    return wrapper_debug

def sub_level(level: str or str, *, tag: str = '-------------- level: {0}', signature: bool = True):
    """
        Print the function signature [Optional] and return value.

    :param signature: for sub-level method chains, prints it's signature. defaults to true.
    :param level: the call stack level. f() -> g() -> h() -> etc.
    :param tag: a unique string to identify the output in the console window. must have one '{0}' for str.format() support.
    :return:
    """
    def sub(func: callable):
        """
        :param func: callable function to be debugged.
        :return:
        """
        name = GetFunctionName(func)

        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            print_chain_signature(func, tag, level, signature, *args, **kwargs)
            result = func(*args, **kwargs)
            print(f"{name}  returned  {result!r}\n")

            return result
        return wrapper_debug
    return sub
