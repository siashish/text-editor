# enrixpad is free software: you can redistribute it and/or modify

# it under the terms of the GNU General Public License as published by

# the Free Software Foundation, either version 3 of the License, or

# (at your option) any later version.





# This program is distributed in the hope that it will be useful,

# but WITHOUT ANY WARRANTY; without even the implied warranty of

# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

# GNU General Public License for more details.





# You should have received a copy of the GNU General Public License

# along with this program. If not, see <http://www.gnu.org/licenses/>.



# -*- coding: cp1252 -*-

from Tkinter import *

import tkFileDialog

import tkMessageBox

from tkColorChooser import askcolor

import datetime

import webbrowser

from tkFileDialog import askopenfilename, asksaveasfilename


def line():
    lin = "_" * 60

    text.insert(INSERT, lin)


def date():
    data = datetime.date.today()

    text.insert(INSERT, data)


def normal():
    text.config(font=("Arial", 10))


def bold():
    text.config(font=("Arial", 10, "bold"))


def underline():
    text.config(font=("Arial", 10, "underline"))


def italic():
    text.config(font=("Arial", 10, "italic"))


def font():
    (triple, color) = askcolor()

    if color:
        text.config(foreground=color)


def kill():
    root.destroy()


def about():
    pass


def opn():
    text.delete(1.0, END)

    file = open(askopenfilename(), 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT, txt)

    else:

        pass


def save():
    filename = asksaveasfilename()

    if filename:
        alltext = text.get(1.0, END)

        open(filename, 'w').write(alltext)


def copy():
    text.clipboard_clear()

    text.clipboard_append(text.selection_get())


def paste():
    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Errore", "Gli appunti sono vuoti!")


def clear():
    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)


def clearall():
    text.delete(1.0, END)


def background():
    (triple, color) = askcolor()

    if color:
        text.config(background=color)


def about():
    ab = Toplevel(root)

    txt = "Enrix's pad\nRealizzato da Enrix (C)\n http://www.enrixweb.altervista.org\nIl programma è rilasciato sotto licensa GPL"

    la = Label(ab, text=txt, foreground='blue')

    la.pack()


def web():
    webbrowser.open('http://www.enrixweb.altervista.org')


root = Tk()

root.title("Enrix's pad")

menu = Menu(root)

filemenu = Menu(root)

root.config(menu=menu)

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Apri...", command=opn)

filemenu.add_command(label="Salva...", command=save)

filemenu.add_separator()

filemenu.add_command(label="Esci", command=kill)

modmenu = Menu(root)

menu.add_cascade(label="Modifica", menu=modmenu)

modmenu.add_command(label="Copia", command=copy)

modmenu.add_command(label="Incolla", command=paste)

modmenu.add_separator()

modmenu.add_command(label="Cancella selezione", command=clear)

modmenu.add_command(label="Cancella Tutto", command=clearall)

insmenu = Menu(root)

menu.add_cascade(label="Inserisci", menu=insmenu)

insmenu.add_command(label="Data", command=date)

insmenu.add_command(label="Linea", command=line)

formatmenu = Menu(menu)

menu.add_cascade(label="Formato", menu=formatmenu)

formatmenu.add_cascade(label="Colore...", command=font)

formatmenu.add_separator()

formatmenu.add_radiobutton(label='Normale', command=normal)

formatmenu.add_radiobutton(label='Grassetto', command=bold)

formatmenu.add_radiobutton(label='Sottolineato', command=underline)

formatmenu.add_radiobutton(label='Corsivo', command=italic)

persomenu = Menu(root)

menu.add_cascade(label="Personalizza", menu=persomenu)

persomenu.add_command(label="Sfondo...", command=background)

helpmenu = Menu(menu)

menu.add_cascade(label="?", menu=helpmenu)

helpmenu.add_command(label="Info su Snackepad", command=about)

helpmenu.add_command(label="Website", command=web)

text = Text(root, height=30, width=60, font=("Arial", 10))

scroll = Scrollbar(root, command=text.yview)

scroll.config(command=text.yview)

text.config(yscrollcommand=scroll.set)

scroll.pack(side=RIGHT, fill=Y)

text.pack()

root.resizable(0, 0)

root.mainloop()