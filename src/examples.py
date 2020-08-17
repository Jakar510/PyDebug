import time
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

        @check_time
        def timed(self, *args, **kwargs):
            time.sleep(1)

        @Chains.chain()
        def root(self, *args, **kwargs):
            self.sub1(*args, **kwargs)
        @Chains.sub()
        def sub1(self, *args, **kwargs):
            self.sub2(*args, **kwargs)

        @Chains.sub()
        def sub2(self, *args, **kwargs):
            pass



    t = test()

    t.run()
    t.timed()
    t.pp_run()

    evt = tk.Event()
    evt.widget = None
    evt.x = None
    evt.y = None
    t.tk_run(evt)

    t.root()
