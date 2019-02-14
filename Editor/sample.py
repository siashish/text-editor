import tkinter
from tkinter import *



class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class CustomText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result



class Example(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        self.text.insert("end",self.text)



    def _on_change(self, event):
        self.linenumbers.redraw()

if __name__ == "__main__":
    root = Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()




#run function

import sys
import inspect
import importlib
import os

if __name__ == "__main__":
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)

    # get the second argument from the command line
    methodname = sys.argv[1]

    # split this into module, class and function name
    modulename, classname, funcname = methodname.split(".")

    # get pointers to the objects based on the string names
    themodule = importlib.import_module(modulename)
    theclass = getattr(themodule, classname)
    thefunc = getattr(theclass, funcname)

    # pass all the parameters from the third until the end of
    # what the function needs & ignore the rest
    args = inspect.getargspec(thefunc)
    z = len(args[0]) + 2
    params=sys.argv[2:z]
    thefunc(*params)