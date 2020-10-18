# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:11:54 2020

@author: Scruffydrew
"""
global x, y
import mouse
import tkinter as tkr


root = tkr.Tk()

root.overrideredirect(1)
root.wm_attributes("-topmost", 1)
root.geometry("200x200")

root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
root.bind('<ButtonRelease-1>', lambda e: standard_bind())                     

def standard_bind():
    root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
    # allows for window to be dragged
def event(widget, Mode=False):
    global x, y
    if Mode:
        x = widget.x
        y = widget.y
    root.bind('<B1-Motion>', lambda e: event(e))
    root.geometry('+%d+%d' % (mouse.get_position()[0]-x, mouse.get_position()[1]-y))
    
    ScreenWidth = root.winfo_screenwidth()
    ScreenHeight = root.winfo_screenheight()

    print('Screen Width =', ScreenWidth)
    print('Screen Height =', ScreenHeight)

    WindowWidth = root.winfo_width()
    WindowHeight = root.winfo_height()

    print('Window Width =', WindowWidth)
    print('Window Height =', WindowHeight)

    WindowX = root.winfo_x()
    WindowY = root.winfo_y()

    print('Window X =', WindowX)
    print('Window Y =', WindowY)
    
    if WindowX <= int(-1921):
        WindowX = int(-1920)
        root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
        root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
        root.bind('<ButtonRelease-1>', lambda e: standard_bind())
        
    if WindowX >= int(1721):
        WindowX = int(1720)
        root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))  
        root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
        root.bind('<ButtonRelease-1>', lambda e: standard_bind())
        
    if WindowY <= int(-1):
        WindowY = int(0)
        root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
        root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
        root.bind('<ButtonRelease-1>', lambda e: standard_bind())
        
    if WindowY >= int(881):
        WindowY = int(880)
        root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY)) 
        root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
        root.bind('<ButtonRelease-1>', lambda e: standard_bind())

ScreenWidth = root.winfo_screenwidth()
ScreenHeight = root.winfo_screenheight()
    
root.mainloop()