# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:51:18 2020

@author: Scruffydrew
"""
import os
global x, y
import mouse
import keyboard
import pyautogui
import tkinter as tkr
from PIL import Image, ImageTk
from pynput.keyboard import Listener
from cryptography.fernet import Fernet
from tkinter import messagebox as mbox

root = tkr.Tk()

    # setup for Tk root window
    # makes the Tk root window always appear on top
root.wm_attributes("-topmost", 1)
    # names the Tk root window
root.title("Image Selector")
    # sets the size of the window
root.geometry("600x360")

    # gets the current directory containing the python file
Dir = os.getcwd()
    # determine the suffix of image and adds it to a list
extension = ".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp", ".esp", ".icns", ".ico", ".im", ".jfif", ".msp", ".pcx", ".sgi", ".spider", ".webp", ".xbm", ".blp", ".cur", ".dcx", ".dds", ".fli", ".flc", ".fpx", ".ftex", ".gbr", ".gd", ".imt", ".iptc", ".naa", ".mcidas", ".mic", ".mpo", ".pcd", ".pixar", ".psd", ".tga", ".wal", ".xpm", ".PNG", ".JPG", ".JPEG", ".GIF", ".TIFF", ".BMP", ".ESP", ".ICNS", ".ICO", ".IM", ".JFIF", ".MSP", ".PCX", ".SGI", ".SPIDER", ".WEBP", ".XBM", ".BLP", ".CUR", ".DCX", ".DDS", ".FLI", ".FLC", ".FPX", ".FTEX", ".GBR", ".GD", ".IMT", ".IPTC", ".NAA", ".MCIDAS", ".MIC", ".MPO", ".PCD", ".PIXAR", ".PSD", ".TGA", ".WAL", ".XPM"
file = [_ for _ in os.listdir(Dir) if _.endswith(extension)]
#print(file)##################################################################
#print(file[1])###############################################################

def showimg(e):
    lab.lift()
    n = lst.curselection()    # returns the name of current selected item in list
    fname = lst.get(n)
    file_path = os.path.join(Dir, fname)    # combines directory with ImageName to create image path
    file_name, file_extension = os.path.splitext(file_path)     # splits image path up into two variables
    desiredHeight = 240     # desired height of thumbnail
    desiredWidth = 240      # desired width of thumbnail
    img = Image.open(fname)
    if img.size[1] >= img.size[0]:      # if the height is greater than the width:
        changesize = 1
    else:
        changesize = 2
    if changesize == 1:
        if float(img.size[1]) >= desiredHeight:     # if the height is greater than the desired height of the thumbnail
            change = 1
        else:
            change = 2
    else:
        if float(img.size[0]) >= desiredWidth:      # if the width is greater than the desired width of the thumbnail
            change = 0
        else:
            change = 2
    if change == 1:     # reduce size of image via height
        hpercent = (desiredHeight/float(img.size[1]))
        wsize = int((float(img.size[0])*float(hpercent)))
        thumbimg = img.resize((wsize,desiredHeight), Image.ANTIALIAS)
        thumbimg.save('resized.png')
        thumbimage = tkr.PhotoImage(file='resized.png')
    elif change == 0:   # reduce size of image via width
        wpercent = (desiredWidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        thumbimg = img.resize((desiredWidth,hsize), Image.ANTIALIAS)
        thumbimg.save('resized.png')
        thumbimage = tkr.PhotoImage(file='resized.png')
    else:
        thumbimage = tkr.PhotoImage(file=fname)
    labimg = thumbimage
    lab.config(image=labimg)
    lab.image = labimg
    ImageName = fname
    return ImageName
    return thumbimage
   
def hide():
        # deletes decrypted files
    os.remove('Background.PNG')
    os.remove('Format.PNG')
    os.remove('resized.png')

        # creates bind for movement of mouse
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
    
        ScreenWidth = root.winfo_screenwidth()  # screen width
        ScreenHeight = root.winfo_screenheight()    # screen height

        #print('Screen Width =', ScreenWidth)#################################
        #print('Screen Height =', ScreenHeight)###############################

        WindowWidth = root.winfo_width()    # window width
        WindowHeight = root.winfo_height()  # window height

        #print('Window Width =', WindowWidth)#################################
        #print('Window Height =', WindowHeight)###############################

        WindowX = root.winfo_x()    # window X position
        WindowY = root.winfo_y()    # window Y position

        #print('Window X =', WindowX)#########################################
        #print('Window Y =', WindowY)#########################################
    
        #while True: print(pyautogui.position())##############################
        mouseX, mouseY = pyautogui.position()
        #print('Mouse X =', mouseX)###########################################
        #print('Mouse Y =', mouseY)###########################################
            # keeps window on screen
        if WindowX <= int(-ScreenWidth + WindowWidth - 1):
            WindowX = int((-1*ScreenWidth) + WindowWidth)
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
            root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
            root.bind('<ButtonRelease-1>', lambda e: standard_bind())
        
        if WindowY >= int(ScreenHeight - WindowHeight + 1):
            WindowY = int(ScreenHeight - WindowHeight)
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY)) 
            root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
            root.bind('<ButtonRelease-1>', lambda e: standard_bind())            
        
        if WindowX >= int(ScreenWidth - WindowWidth + 1):
            WindowX = int(ScreenWidth - WindowWidth)
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))  
            root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
            root.bind('<ButtonRelease-1>', lambda e: standard_bind())
            
        if WindowY <= int(-1):
            WindowY = int(0)
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
            root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
            root.bind('<ButtonRelease-1>', lambda e: standard_bind())
            #   keeps mouse on window when dragging window
        if mouseX <= (WindowX):
            WindowX = mouseX-5
            WindowY = WindowY+5
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
            #print(mouseX)####################################################
        if mouseX >= (WindowX + WindowWidth):
            WindowX = (mouseX-WindowWidth+5)
            WindowY = WindowY-5
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
            #print(mouseX)####################################################
        if mouseY <= (WindowY):
            WindowY = mouseY-5
            WindowX = WindowX+5
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
            #print(mouseY)####################################################
        if mouseY >= (WindowY + WindowHeight):
            WindowY = (mouseY-WindowWidth+5)
            WindowX = WindowX-5
            root.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, WindowX, WindowY))
            #print(mouseY)####################################################

    imgName = showimg(fname)    # get variable 'ImageName' from showimg
    thumbnailname = 'resized.png'
    thumbnail = os.path.join(Dir, thumbnailname)    # combines directory path with thumbnail name to create thumbnail path
    filename = os.path.join(Dir, imgName)    # combines directory with image name to create image path
        # removes all elements on the window
    for ele in root.winfo_children():
        ele.destroy()

    if file != []:  # if list is not empty:
        os.remove(thumbnail)    # deletes the thumbnail image used when selecting the desired image
            # names the Tk root window
        root.title("Image Displayer")
            # removes the title bar from the Tk root window
        root.overrideredirect(1)
            # gets the size of the image
        image = Image.open(imgName)
        width, height = image.size
        w = width  # width of the image
        h = height  # height of the image
        X = -w  # X position on screen
        Y = 0  # Y position on screen
            # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen
            # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        #print(ws, hs, x, y, w, h, X, Y)######################################
        if w >= (ws+1):    # reduce size of image via height
            hpc = (ws/float(h))
            wsiz = int((float(w)*float(hpc)))
            Desiredimg = image.resize((wsiz,hs), Image.ANTIALIAS)
            Desiredimg.save('DisplayIMG.png')
            Desiredimage = tkr.PhotoImage(file='DisplayIMG.png')
        elif h >= (hs+1):   # reduce size of image via width
            wpc = (ws/float(w))
            hsiz = int((float(h)*float(wpc)))
            Desiredimg = image.resize((ws,hsiz), Image.ANTIALIAS)
            Desiredimg.save('DisplayIMG.png')
            Desiredimage = tkr.PhotoImage(file='DisplayIMG.png')
        else:
            Desiredimage = tkr.PhotoImage(file=filename)
            # allows for window to be dragged
        root.bind('<B1-Motion>', lambda e: event(e, Mode=True))
        root.bind('<ButtonRelease-1>', lambda e: standard_bind())
        
            # set the dimensions of the screen and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, X, Y))
            # sets image to a label
        imgfinal = Desiredimage
            # creates label to display image on
        lbl = tkr.Label(root, image = imgfinal)
        lbl.image = imgfinal
        lbl.pack()
        return x, y
        #print('x,y returned')################################################
        #print('x,y to be returned')##########################################
    else:
            # error window execution
        root.withdraw()
        mbox.showerror("ERROR", "Image was found but was unable to display it")
        raise SystemExit

    # if image can't be found an error message will appear
if file == []:   # if list is empty:
        # error window execution
    root.withdraw()
    mbox.showerror("ERROR", "Image could not be found")
    raise SystemExit
else:
        # Run GUI code
        # reads the encryption key
    keyfile = open('key.key', 'rb')  # open the file as wb to read bytes
    key = keyfile.read()  # the key will be type bytes
        # decrypts the image
    eFormat_file = 'Format.encrypted'
    Format_file = 'Format.PNG'

    with open(eFormat_file, 'rb') as f:
        data = f.read()  # read the bytes of the encrypted image

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(Format_file, 'wb') as f:
            f.write(decrypted)  # write the decrypted bytes to the output file

    except InvalidToken as e:
            # error window execution
        root.withdraw()
        mbox.showerror("ERROR", "An ERROR has occured please reinstall the program")
        raise SystemExit

        # decrypts the image
    eBackground_file = 'Background.encrypted'
    Background_file = 'Background.PNG'

    with open(eBackground_file, 'rb') as f:
        data = f.read()  # read the bytes of the encrypted image

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(Background_file, 'wb') as f:
            f.write(decrypted)  # write the decrypted bytes to the output file
            keyfile.close()
    except InvalidToken as e:
            # error window execution
        root.withdraw()
        mbox.showerror("ERROR", "An ERROR has occured please reinstall the program")
        raise SystemExit
    #print(file)##############################################################
    for fname in file:
        if fname == 'Background.PNG':
            file.remove('Background.PNG')
            #print(file)######################################################
    for fname in file:
        if fname == 'Format.PNG':
            file.remove('Format.PNG')
            #print(file)######################################################
    for fname in file:
        if fname == 'resized.png':
            file.remove('resized.png')
            #print(file)######################################################
    #print(file)##############################################################
        # displays image as background
    C = tkr.Canvas(root, bg="blue", height=600, width=360)
    BG = os.path.join(Dir, "Background.PNG")
    filename = tkr.PhotoImage(file = BG)
    background_label = tkr.Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
    C.place()
        # create GUI for selection of image
    lst = tkr.Listbox(root)     # displays list on GUI
    lst.grid(column=0, row=0, rowspan=4, sticky=tkr.N+tkr.S, padx=5, pady=5)
        # bind each item in list to its respected image
    for fname in file:
        lst.insert(tkr.END, fname)
        lst.bind('<<ListboxSelect>>', showimg)
        # display respected image on GUI
    img = tkr.PhotoImage()
    lab = tkr.Label(root, image=img, borderwidth=2, relief="solid", bg="white")
    lab.lower()
    lab.grid(column=1, row=2, columnspan=3)
        # display Label on GUI
    lbl = tkr.Label(root, text="Select an Image to display")
    lbl.lower()
    lbl.grid(column=1, row=0, columnspan=2, sticky=tkr.E+tkr.W+tkr.NW, pady=3)
        # display button on GUI
    buttonsub = tkr.Button(root, text='Select', command=hide)
    buttonsub.grid(column=1, row=3, sticky=tkr.SW, padx=2, pady=6)
        # creates formating for GUI
    forlab = tkr.Label(root)
    forlab.lower()
    forlab.grid(column=4, row=0, rowspan=4, pady=50, sticky=tkr.N+tkr.E+tkr.S+tkr.W)
    forlab1 = tkr.Label(root)
    forlab1.lower()
    forlab1.grid(column=3, row=0, padx=50, sticky=tkr.N+tkr.E+tkr.S+tkr.W)
    ForI1 = os.path.join(Dir, 'Format.PNG')
    forimg1 = tkr.PhotoImage(file=ForI1)
    fortimg = tkr.Label(root, image=forimg1)
    fortimg.lower()
    fortimg.grid(column=1, row=2, columnspan=3)



root.mainloop()