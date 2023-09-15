import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_app=tk.Tk()
main_app.geometry('1200x800')
main_app.title("Word Editor")



########################################### Menu ###########################################
main_menu=tk.Menu()

# file dropdown menu icons 
new_icon=tk.PhotoImage(file='icon/new.png')
open_icon=tk.PhotoImage(file='icon/open.png')
saveas_icon=tk.PhotoImage(file='icon/save_as.png')
exit_icon=tk.PhotoImage(file='icon/exit.png')
save_icon=tk.PhotoImage(file='icon/save.png')

file=tk.Menu(main_menu,tearoff=False)
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Save As',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')

# Edit dropdown menu icons
copy_icon=tk.PhotoImage(file='icon/copy.png')
paste_icon=tk.PhotoImage(file='icon/paste.png')
cut_icon=tk.PhotoImage(file='icon/cut.png')
clearall_icon=tk.PhotoImage(file='icon/clear_all.png')
find_icon=tk.PhotoImage(file='icon/find.png')

edit=tk.Menu(main_menu,tearoff=False)
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=clearall_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C')
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')

# View dropdown menu icons 
toolbar_icon=tk.PhotoImage(file='icon/tool_bar.png')
statusbar_icon=tk.PhotoImage(file='icon/status_bar.png')

view=tk.Menu(main_menu,tearoff=False)
view.add_checkbutton(label="Tool Bar",image=toolbar_icon,compound=tk.LEFT,accelerator='')
view.add_checkbutton(label="Status Bar",image=statusbar_icon,compound=tk.LEFT,accelerator='')

color=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color)












main_app.config(menu=main_menu)
# -------------------------------------------Menu Ending-------------------------------------








main_app.mainloop()
