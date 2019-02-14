import tkinter
from tkinter import *
import sys
import tkinter as ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import colorchooser
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
from tkinter.font import *
import tkinter.ttk as ttk

import datetime
import webbrowser
import os
import inspect
import importlib


file = None
def Quit():
    def opn():

        text.delete(1.0, END)

        global file
        file = open(askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*"),("Text files","*.txt"),("Python files","*.py") )))

        if file != '':
            x = str(file)
            y = x.split()[1]
            z = y.split("\'")[1]
            v=z.split("\\")[-1]
            t.title(os.path.basename(v)+"- Ashish's text")
            txt = file.read()

            text.insert(INSERT, txt)
            file.close()
        else:

            pass

    def new_file():
        t.title("Untitled - Ashish's text")

        text.delete(1.0,END)
        file=None

    def save():
        filename = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*"),("Text files","*.txt"),("Python files","*.py") ))

        if filename:
            alltext = text.get(1.0, END)

            f=open(filename, 'w')
            f.write(alltext)
            x = str(f)
            # print(x)
            # print(f)
            y = x.split()[1]
            z = y.split("/")[-1]
            # print("value of z=",z)
            # v = z.split("\\")
            # print("val of v=",v)
            # c=v.split("\\")
            # print("Value of c: ",c)

            t.title(z+"- Ashish's text")




    def show():
        ab=Toplevel(t)
        ab.iconbitmap(r'letter-g-icon-png-21704-Windows.ico')
        ab.title("Information")
        l=Label(ab,text="Ashish's text\nauthor and developer-Ashish(the decider)",fg="cyan",bg="grey",font=("Elephant",20))
        ab.geometry("580x90")
        l.pack()
        # showinfo("Ashish's text","author and developer-Ashish(the decider)")

    def normal():
        text.config(font=("Arial", 20))

    def bold():
        text.config(font=("Arial", 20, "bold"))

    def underline():
        text.config(font=("Arial", 20, "underline"))

    def italic():
        text.config(font=("Arial", 20, "italic"))

    def fontcolor():
        (triple, color) = askcolor()

        if color:
            text.config(foreground=color)

    def fontstyle():
        font=families("arial","helvetica")

        if font:
            text.config(font="font")

    def background():
        (triple, color) = askcolor()

        if color:
            text.config(background=color)

    def delete():
        MsgBox = messagebox.askquestion('Delete File', 'Are you sure you want to delete the file?',icon='warning')
        if MsgBox == 'yes':
            x = str(file)
            y = x.split()[1]
            t.destroy()

            y.split("\'")[1]
            os.remove(y.split("\'")[1])
            Quit()
            # os.remove(os.path.curdir)

        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')

    def shw(event):
        y = ''
        x = text.index("end").split(".")[0]

        for i in range(1, int(x)):
            y += str(i) + '\n'

        text1.config(state='normal')
        text1.delete(1.0, 'end')
        text1.insert(1.0, y)
        text1.config(state='disabled')
        display()

    def display():
        x, y = text.index(INSERT).split('.')
        str = 'Line ' + x + '| Column' + y
        label.config(text=str)



    def find():
        ad=Toplevel(t)
        ad.title("Find Text")
        ad.iconbitmap(r'letter-g-icon-png-21704-Windows.ico')
        ad.geometry("480x90")
        l1=Label(ad,bg="light grey",text="enter the text you want to find.")
        l1.pack()
        e=Entry(ad,bg="light cyan")
        e.pack()

        def search():
            start = 1.0
            while 1:
                pos = text.search(e.get(), start, stopindex=END)
                if not pos:
                    break
                text.tag_config(e.get())
                print(pos)
                start = pos + "+1c"

        v1 = Button(ad, bd=4, width=5, height=1, text="OK", font=15, command=search)
        v1.pack()
        mainloop()







    t=Toplevel()                                   #child window including all functionality
    t.title("Untitled - Ashish's Text")
    screenwidth=t.winfo_screenwidth()
    screenheight=t.winfo_screenheight()
    t.grid_rowconfigure(0,weight=1)
    t.grid_columnconfigure(0,weight=1)
    t.geometry('600x600')
    toolbaar = Frame(t, bd=2, relief=RAISED,bg="white")     #Frame for icons

    img = Image.open(r"new.jpg")                           #icon for new file
    photo1 = ImageTk.PhotoImage(img)
    new = Button(toolbaar, bd=5,bg="white", width=22,height=22, relief=FLAT,image=photo1,command=new_file)
    new.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"open.jpg")                          #icon for open new file
    photo2 = ImageTk.PhotoImage(img)
    open1=Button(toolbaar, bd=5,bg="grey", width=22,height=22, relief=FLAT,image=photo2,command=opn)
    open1.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"cut.jpg")                          #icon for cut
    photo3 = ImageTk.PhotoImage(img)
    cut=Button(toolbaar, bd=5,bg="grey", width=22,height=22, relief=FLAT,image=photo3,command=lambda :t.focus_get().event_generate("<<Cut>>"))
    cut.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"copy.png")                        #icon for copy
    photo4 = ImageTk.PhotoImage(img)
    copy = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo4,command=lambda: t.focus_get().event_generate("<<Copy>>"))
    copy.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"paste.jpg")                         #icon for paste
    photo5 = ImageTk.PhotoImage(img)
    paste = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo5,command=lambda: t.focus_get().event_generate("<<Paste>>"))
    paste.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"find.jpg")                         #icon that helps find position of text item
    photo6 = ImageTk.PhotoImage(img)
    find = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo6,command=find)
    find.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"info.png")                        #info
    photo7 = ImageTk.PhotoImage(img)
    info1 = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo7,command=show)
    info1.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"undo.png")                        #icon for undo operation
    photo8 = ImageTk.PhotoImage(img)
    undo = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo8,command=lambda:t.focus_get().event_generate("<<Undo>>"))
    undo.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"redo.jpg")                        #icon for redo operation
    photo9 = ImageTk.PhotoImage(img)
    redo = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo9,command=lambda:t.focus_get().event_generate("<<Redo>>"))
    redo.pack(side=LEFT, padx=2, pady=2)


    toolbaar.pack(side=TOP, fill=X)

    #code for line number finding

    text1 = Text(t, bg='powderblue', fg='black', state='disabled', width=3)
    text1.pack(side=LEFT, fill=Y)

    label = Label(t, text="Line 0| Column 0", bg='powderblue', fg='black')
    label.pack(side=BOTTOM,anchor=SE)

    text = Text(t,  font=("Arial", 10),height=700)

    scroll = Scrollbar(t, command=text.yview)

    scroll.config(command=text.yview)

    text.config(yscrollcommand=scroll.set,bg="white")

    scroll.pack(side=RIGHT, fill=Y)

    text.pack(side=TOP,fill=BOTH)

    t.iconbitmap(r'letter-g-icon-png-21704-Windows.ico')
    text.bind("<Key>", shw)
    # t.pack(fill=BOTH,expand=1)
    menu=Menu(t)                        #main menu for editor
    t.config(menu=menu,bg="light grey")


    filemenu=Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New             ",accelerator='Ctrl+N',command=new_file)
    filemenu.add_command(label="Open            ",accelerator='Ctrl+O',command=opn)
    filemenu.add_command(label="Save            ",accelerator="Ctrl+S",command=save)
    filemenu.add_command(label="Close"           ,accelerator='Ctrl+W',command=t.quit)

    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=t.quit)

    editmenu=Menu(menu)
    menu.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label='Cut             ',accelerator='Ctrl+X',command=lambda :t.focus_get().event_generate("<<Cut>>"))
    editmenu.add_command(label='Copy            ',accelerator='Ctrl+C',command=lambda :t.focus_get().event_generate("<<Copy>>"))
    editmenu.add_command(label='Paste           ',accelerator='Ctrl+V',command=lambda :t.focus_get().event_generate("<<Paste>>"))
    editmenu.add_command(label='Delete'          ,accelerator='Ctrl+Alt+D',command=delete)
    editmenu.add_command(label='Undo'            ,accelerator='Ctrl+Z',command=lambda:t.focus_get().event_generate("<<Undo>>"))
    editmenu.add_command(label='Redo'           ,accelerator='Ctrl+Y',command=lambda :t.focus_get().event_generate("<<Redo>>"))

    formatmenu=Menu(menu)
    menu.add_cascade(label='Format',menu=formatmenu)
    formatmenu.add_checkbutton(label='Normal',command=normal)
    formatmenu.add_checkbutton(label='Bold',command=bold)
    formatmenu.add_checkbutton(label='Underline',command=underline)
    formatmenu.add_checkbutton(label='Italic',command=italic)
    formatmenu.add_separator()
    formatmenu.add_command(label='set font color',command=fontcolor)
    formatmenu.add_command(label='set font style',command=fontstyle)
    formatmenu.add_command(label='set background color',command=background)

    runmenu=Menu(menu)
    menu.add_cascade(label="Run",menu=runmenu)
    runmenu.add_command(label="Run...           F5")
    runmenu.add_separator()
    runmenu.add_command(label="Launch in firefox            Ctrl+alt+Shift+X")
    runmenu.add_command(label="Launch in Chrome             Ctrl+alt+Shift+R")

    helpmenu=Menu(menu)
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="About Ashish's Text..",command=show)

    






    root.withdraw()
    mainloop()

root=Tk()                       #root window
style=ttk.Style(root)
root.title("Ashish's Text")    #title of root
root.config(bg="light grey")    #background color
screenwidth=root.winfo_screenwidth()       #auto adjust of width and height
screenheight=root.winfo_screenheight()
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.geometry("600x600")
root.iconbitmap(r'letter-g-icon-png-21704-Windows.ico')         #setting icon of window
# root.resizable("False","False")
im=Image.open(r"ashish.jpg")
photo=ImageTk.PhotoImage(im)

# cv = Canvas()
# cv.config(width=600,height=600)
# cv.place( x=0,y=0,relwidth=1,relheight=1)


# cv.create_image(50, 50, image=photo)
l=Label(image=photo)                      #inserting main image
l.place(x=0,y=0,relwidth=1,relheight=1)

b=Button(l,justify=LEFT,bd=5,width=60,bg="grey",command=Quit)    #button forming
img=Image.open(r"jf.jpg")                                        #inserting image into button
photo2=ImageTk.PhotoImage(img)
b.config(image=photo2)
# cv.create_window(200,200,anchor="center",window=b)
b.pack()




root.mainloop()