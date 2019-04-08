import roboticshours
from tkinter import *

root = Tk()
root.title("Names")

mainframe = Frame(root)
mainframe.grid(column=2,row=2)
mainframe.columnconfigure(2, weight = 1)
mainframe.rowconfigure(2, weight = 1)
mainframe.pack(pady = 200, padx = 100)

tkvar = StringVar(root)

#######################################
choices = {'Nathan','Thomas','Evan','Josiah','Drew','Tyler'}
tkvar.set('Tyler')

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose your fighter").grid(row = 0, column = 1)
popupMenu.grid(row = 1, column =1)

def change_dropdown(*args):
    print( tkvar.get() )

tkvar.trace('w', change_dropdown)
#######################################
def callback():
    print ("Submitted!")

f = Frame(root, height=40, width=80)
f.pack_propagate(0) # don't shrink
f.pack()

b = Button(f, text="SUBMIT", command=callback)
b.grid(row = 2, column = 1)
b.pack()

#######################################

root.mainloop()