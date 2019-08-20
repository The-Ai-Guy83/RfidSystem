#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Jun 13, 2019 03:15:43 PM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Schritt3_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Schritt3_support.set_Tk_var()
    top = Toplevel1 (root)
    Schritt3_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Schritt3_support.set_Tk_var()
    top = Toplevel1 (w)
    Schritt3_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1440x837+485+226")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.TSizegrip2 = ttk.Sizegrip(top)
        self.TSizegrip2.place(anchor='se', relx=1.0, rely=1.0)

        self.TSizegrip3 = ttk.Sizegrip(top)
        self.TSizegrip3.place(anchor='se', relx=1.0, rely=1.0)

        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton1 = ttk.Radiobutton(top)
        self.TRadiobutton1.place(relx=0.049, rely=0.167, relwidth=0.119
                , relheight=0.0, height=21)
        self.TRadiobutton1.configure(takefocus="")
        self.TRadiobutton1.configure(text='''Soll gerade angemeldet sein''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.09, rely=0.119, relheight=0.025
                , relwidth=0.088)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.049, rely=0.131, height=19, width=36)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Klasse''')

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.083, rely=0.311, relwidth=0.257
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="370")
        self.TProgressbar1.configure(variable=Schritt3_support.probar)
        self.TProgressbar1.configure(value="1.0")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.181, rely=0.454, height=25, width=76)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Fertig''')
        self.TButton1.configure(command=)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.014, rely=0.358, relwidth=0.396)



if __name__ == '__main__':
    vp_start_gui()