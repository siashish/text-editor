# import os
#
# fileName = open(r'C:\Users\user\Desktop\gv.txt')
#
# x = str(fileName)
# print(x)
# y = x.split()[1]
# print(y)
# z=y.split("\'")[1]
# print(z)
# print(z.split("\\")[-1])
# # print(os.path.curdir)
# fileName.close()
#
text.insert(END, "hello, world")

start = 1.0
while 1:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print(pos)
    start = pos + "+1c"

import tkinter
from tkinter import *
root=Tk()

# t = Text(root)
# t.pack()
# t.insert(END, '''\
# blah blah blah Failed blah blah
# blah blah blah Passed blah blah
# blah blah blah Failed blah blah
# blah blah blah Failed blah blah
# ''')
# t.tag_config('failed', background='light green')
# t.tag_config('passed', background='blue')
#
# def search(text_widget, keyword, tag):
#     pos = '1.0'
#     while True:
#         idx = text_widget.search(keyword, pos, END)
#         if not idx:
#             break
#         pos = '{}+{}c'.format(idx, len(keyword))
#         text_widget.tag_add(tag, idx, pos)
#
# search(t, 'Failed', 'failed')
# search(t, 'Passed', 'passed')
#
# #t.tag_delete('failed')
# #t.tag_delete('passed')
#
# root.mainloop()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()