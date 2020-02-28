import logging
import pprint

pp = pprint.PrettyPrinter(indent=4)

__all__ = ['PRINT', 'getPPrintStr', 'pp']

def PRINT(title: str, Object: any, logger: logging.Logger = None):
    print(f"\n ---------------- {title} ---------------- \n\r")
    pp.pprint(Object)
    if logger: logger.debug(f' ---------------- {title} ---------------- \n{pp.pformat(Object)}')


def getPPrintStr(Object: any) -> str:
    return f'{pp.pformat(Object)}'

