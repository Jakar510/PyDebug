import tkinter as tk
from PyDebug import *

if __name__ == '__main__':

    class test(object):
        @pprint_debug
        def pp_run(self, *args, **kwargs):
            pass
        @debug
        def run(self, *args, **kwargs):
            pass
        @debugTkinterEvent
        def tk_run(self, event: tk.Event):
            pass

    t = test()

    t.run()

    t.pp_run()

    evt = tk.Event()
    evt.widget = None
    evt.x = None
    evt.y = None
    t.tk_run(evt)

