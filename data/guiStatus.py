
from tkinter import  *
from jsonFunc import jsonFunc

root = Tk()



menubar = Menu(root)
a = jsonFunc.retornoNotificacaoAluno(100)
label1 = Label(text = "Notificações",bg = "#ff0000"#0099ff",
 ,font=("Caviar Dreams",16),height = 2, anchor='w',fg="#000042")
label1.pack(side = TOP, fill = BOTH)
varCor = 6750156
for pessoas in a:
    print(type(pessoas))
    print(pessoas)

    b = Label(root, text = str(pessoas), font=("Caviar Dreams", 12),fg="#000042",
    bg ="#" + str(hex(varCor))[2:] ,    anchor='w',relief= RAISED, padx = 5)

    varCor+= 111111
    #c = Label( anchor='w')
    b.pack(side=TOP, fill = BOTH)
    #c.pack(side=TOP)
root.title("Auto SEGE Manager")
root.mainloop()

"""
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
"""
