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


# Edit dropdown menu icons
copy_icon=tk.PhotoImage(file='icon/copy.png')
paste_icon=tk.PhotoImage(file='icon/paste.png')
cut_icon=tk.PhotoImage(file='icon/cut.png')
clearall_icon=tk.PhotoImage(file='icon/clear_all.png')
find_icon=tk.PhotoImage(file='icon/find.png')

edit=tk.Menu(main_menu,tearoff=False)



# View dropdown menu icons 
toolbar_icon=tk.PhotoImage(file='icon/tool_bar.png')
statusbar_icon=tk.PhotoImage(file='icon/status_bar.png')

view=tk.Menu(main_menu,tearoff=False)



# color theme dropdown menu icons
light_icon=tk.PhotoImage(file='icon/light_default.png')
lightplus_icon=tk.PhotoImage(file='icon/light_plus.png')
dark_icon=tk.PhotoImage(file='icon/dark.png')
red_icon=tk.PhotoImage(file='icon/red.png')
blue_icon=tk.PhotoImage(file='icon/night_blue.png')
color=tk.Menu(main_menu,tearoff=False)





# add cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color)












main_app.config(menu=main_menu)
# -------------------------------------------Menu Ending-------------------------------------




############################################### Tool bar ################################

toolbar=ttk.Label(main_app)
toolbar.pack(side=tk.TOP,fill=tk.X)

# Adding font box
font_tuple=tk.font.families()
fontfamily=tk.StringVar()
font_box=ttk.Combobox(toolbar,textvariable=fontfamily,width=30,state='readonly')
font_box['values']=font_tuple
font_box.grid(row=0,column=0,padx=5)
font_box.current(font_tuple.index('Calibri'))

# ---------------------------------------- Toolbar Ending -------------------------------







######################################### Text editor ###############################
# -------------------------------------- Text editor eding ----------------------------

########################### Main menu functionality #######################

# file commands
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Save As',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')

# edit commands
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=clearall_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C')
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')

# view commands
view.add_checkbutton(label="Tool Bar",image=toolbar_icon,compound=tk.LEFT)
view.add_checkbutton(label="Status Bar",image=statusbar_icon,compound=tk.LEFT)

# color theme commands 
color.add_radiobutton(label='Light(default)',image=light_icon,compound=tk.LEFT)
color.add_radiobutton(label='Light+',image=lightplus_icon,compound=tk.LEFT)
color.add_radiobutton(label='Dark',image=dark_icon,compound=tk.LEFT)
color.add_radiobutton(label='Red',image=red_icon,compound=tk.LEFT)
color.add_radiobutton(label='Blue',image=blue_icon,compound=tk.LEFT)


# -------------------------- ending-----------------------------------






main_app.mainloop()
