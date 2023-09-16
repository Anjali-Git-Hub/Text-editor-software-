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

# adding size box
size_val=tk.IntVar()
size_box=ttk.Combobox(toolbar,textvariable=size_val,width=15,state='readonly')
size_box['values']=tuple(range(11,72,2))
size_box.grid(row=0,column=1,padx=5)
size_box.current(4)

# Bold , italics and underline button 
bold_icon=tk.PhotoImage(file='icon/bold.png')
bold_btn=ttk.Button(toolbar,image=bold_icon)
bold_btn.grid(column=2,row=0,padx=5)


italic_icon=tk.PhotoImage(file='icon/italic.png')
italic_btn=ttk.Button(toolbar,image=italic_icon)
italic_btn.grid(column=3,row=0,padx=5)

underline_icon=tk.PhotoImage(file='icon/underline.png')
underline_btn=ttk.Button(toolbar,image=underline_icon)
underline_btn.grid(column=4,row=0,padx=5)


# color theme button
color_icon=tk.PhotoImage(file='icon/font_color.png')
color_btn=ttk.Button(toolbar,image=color_icon)
color_btn.grid(column=5,row=0,padx=5)


# alignleft,alignright,aligncenter button
alignl_icon=tk.PhotoImage(file='icon/align_left.png')
alignl_btn=ttk.Button(toolbar,image=alignl_icon)
alignl_btn.grid(column=6,row=0,padx=5)

alignc_icon=tk.PhotoImage(file='icon/align_center.png')
alignc_btn=ttk.Button(toolbar,image=alignc_icon)
alignc_btn.grid(row=0,column=7,padx=5)

alignr_icon=tk.PhotoImage(file='icon/align_right.png')
alignr_btn=ttk.Button(toolbar,image=alignr_icon)
alignr_btn.grid(row=0,column=8,padx=5)

# ---------------------------------------- Toolbar Ending -------------------------------

##################################### Text editor ######################################
text_editor=tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# adding functionality of size and font box
text_editor.configure(font=('Calibri',19))
current_font_family='Calibri'
current_font_size=19

def change_font_family(event=None):
    global current_font_family
    current_font_family=fontfamily.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_font_size(event=None):
    global current_font_size
    current_font_size=size_val.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font_family)
size_box.bind("<<ComboboxSelected>>",change_font_size)

# adding functionality of bold btn 
print(tk.font.Font(font=text_editor['font']).actual())
def bold_functionality():
    text_prop=tk.font.Font(font=text_editor['font'])
    if text_prop.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_prop.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=bold_functionality)

# adding functionality of italics btn 
def italics_functionality():
    text_prop=tk.font.Font(font=text_editor['font'])
    if text_prop.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_prop.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=italics_functionality)

# adding functionality of Underline btn 
def underline_functionality():
    text_prop=tk.font.Font(font=text_editor['font'])
    if text_prop.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_prop.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=underline_functionality)

# adding functionality of color theme
def color_chooser():
    color_val= tk.colorchooser.askcolor()
    text_editor.configure(fg=color_val[1])

color_btn.configure(command=color_chooser)

# adding functionality of align items
def align_left():
    textcontent=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,textcontent,'left')
def align_center():
    textcontent=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,textcontent,'center')
def align_right():
    textcontent=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,textcontent,'right')


# adding commands to the btns
alignl_btn.configure(command=align_left)
alignr_btn.configure(command=align_right)
alignc_btn.configure(command=align_center)


# -------------------------------------- Text editor eding ----------------------------

############################### Status Bar ######################################

status_bar=ttk.Label(main_app,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)




# ----------------------------------- statusbar end --------------------------------

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
