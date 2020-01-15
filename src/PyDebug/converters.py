import re

__all__ = ['IsAttributePrivate', 'ObjectToDict']


private_or_special_function_searcher = re.compile(r"(^__\w+$)|(^_\w+$)|(^__\w+__$)")
def IsAttributePrivate(attr_name: str) -> bool:
    return private_or_special_function_searcher.search(attr_name) is not None


def ObjectToDict(Object: any, MethodsToSkip: list or tuple = (), *, ShowAll: bool = False) -> dict:
    """
        Returns a dictionary of the public attributes of the given object provided;
        Filter out private or special functions (_private, __SuperPrivate, __special__).

    :param ShowAll:
    :param MethodsToSkip:
    :param Object:
    :return:
    """
    temp = {}
    for key in dir(Object):
        if key in MethodsToSkip: continue
        if ShowAll or IsAttributePrivate(key):
            temp[key] = getattr(Object, key)
    return temp

