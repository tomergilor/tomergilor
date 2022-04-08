"""
########   create label with "Hello World"      ########
########################################################

import Tkinter as tk         #import gui module

root = tk.Tk()

# create a new Label widget
l = tk.Label(root, text="Hello World")

# Place the label widget on screen
l.pack()

# Start the main loop
root.mainloop()

_________________________________________________________


import Tkinter as tk        #import gui module

root = tk.Tk()

tk.Label(root, text="Name:", anchor="w").pack(fill="x")
tk.Entry(root).pack(fill="x")

tk.Label(root,text="Email:", anchor="w").pack(fill="x")
tk.Entry(root).pack(fill="x")

tk.Button(root,text="Go").pack(fill="x")

root.mainloop()
__________________________________________________________

####### print "Ouch" each time i press on the button "Go"


import Tkinter as tk

def print_hello():
    print "Ouch!"

b = tk.Button(text="Go", command=print_hello)
b.pack()

b.mainloop()
____________________________________________________________

### each click on "Go" button the count is add 1


import Tkinter as tk

class App:
    def __init__(self):
        self.top    = tk.Frame()
        self.button = tk.Button(self.top, text="Go", command=self.clicked)
        self.label  = tk.Label(self.top, text="Clicked: 0")

        self.button.pack()
        self.label.pack()
        self.top.pack(ipadx=10, ipady=10)

        self.count = 0

    def clicked(self):
        self.count += 1
        self.label["text"] = "Clicked: %d" % self.count



root = tk.Tk()
app = App()
root.mainloop()


_________________________________________________________________________

import Tkinter as tk

class App:
    def __init__(self):
        self.name   = tk.StringVar()

        self.top    = tk.Frame()
        self.entry  = tk.Entry(self.top, textvar=self.name)
        self.button = tk.Button(self.top, text="Say Hi", command=self.hello)

        self.entry.pack()
        self.button.pack()
        self.top.pack(ipadx=10, ipady=10)

        self.count = 0

    def hello(self):
        print "Hello: %s" % self.name.get()



root = tk.Tk()
app = App()
root.mainloop()

_____________________________________________________________________________

import Tkinter as tk

class App:
    def __init__(self):
        self.count_text  = tk.StringVar()
        self.count_text.set("Clicked 0 times")

        self.top    = tk.Frame()
        self.button = tk.Button(self.top, text="Go", command=self.clicked)
        self.label  = tk.Label(self.top, textvar=self.count_text )

        self.button.pack()
        self.label.pack()
        self.top.pack(ipadx=10, ipady=10)

        self.count = 0

    def clicked(self):
        self.count += 1
        self.count_text.set("Clicked %d times" % self.count)



root = tk.Tk()
app = App()
root.mainloop()

________________________________________________________________________

import Tkinter as tk

class App:
    def __init__(self):
        self.count_text  = tk.StringVar()
        self.entry_text  = tk.StringVar()
        self.entry_text.trace("w", self.textchanged)

        self.count_text.set("0")

        self.top    = tk.Frame()
        self.entry  = tk.Entry(self.top, textvar=self.entry_text)
        self.label  = tk.Label(self.top, textvar=self.count_text)

        self.entry.pack()
        self.label.pack()
        self.top.pack(ipadx=10, ipady=10)

    def textchanged(self, name, idx, op):
        self.count_text.set(len(self.entry_text.get()))



root = tk.Tk()
app = App()
root.mainloop()

_______________________________________________________________________

"""
import Tkinter as tk

class App:
    def __init__(self):
        self.entry_text  = tk.StringVar()

        self.top    = tk.Frame()
        self.entry  = tk.Entry(self.top, textvar=self.entry_text)
        self.label  = tk.Label(self.top, text="...")

        self.entry.pack()
        self.label.pack()
        self.top.pack(ipadx=10, ipady=10)

        self.entry.bind("<<Copy>>", self.copy_handler)

    def copy_handler(self, ev):
        self.label["text"] = "Text Copied..."



root = tk.Tk()
app = App()
root.mainloop()


