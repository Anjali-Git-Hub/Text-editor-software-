import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_app=tk.Tk()
main_app.geometry('1200x800')
main_app.title("Word Editor")



########################################### Menu ###########################################
main_menu=tk.Menu()
file=tk.Menu(main_menu,tearoff=False)
edit=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
color=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color)












main_app.config(menu=main_menu)
# -------------------------------------------Menu Ending-------------------------------------








main_app.mainloop()