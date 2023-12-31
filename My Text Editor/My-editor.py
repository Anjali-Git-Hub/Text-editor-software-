import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_app=tk.Tk()
main_app.geometry('1200x800')
main_app.title("Word Editor")
# 800


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
light_default_icon = tk.PhotoImage(file='icon/light_default.png')
light_plus_icon = tk.PhotoImage(file='icon/light_plus.png')
dark_icon = tk.PhotoImage(file='icon/dark.png')
red_icon = tk.PhotoImage(file='icon/red.png')
monokai_icon = tk.PhotoImage(file='icon/monokai.png')
night_blue_icon = tk.PhotoImage(file='icon/night_blue.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

# add cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

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
size_box['values']=tuple(range(11,73,2))
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

################################# Text Editor ###############################################
text_editor = tk.Text(main_app)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality 
current_font_family = 'Calibri'
current_font_size = 19

def change_font(event=None):
    global current_font_family
    current_font_family = fontfamily.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_val.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
size_box.bind("<<ComboboxSelected>>", change_fontsize)

######## buttons functionality 

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)


## font color functionality 
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

alignl_btn.configure(command=align_left)

## center 
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

alignc_btn.configure(command=align_center)

## right 
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

alignr_btn.configure(command=align_right)


# ----------------------------------------- Text-editor ending -------------------------------


############################### Status Bar ######################################

status_bar = ttk.Label(text_editor,text='Status Bar',anchor='center')
status_bar.pack(side=tk.BOTTOM,fill=tk.X)



# adding functionality of status bar

text_changed = False 
def statusbar_func(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'{words}:Words    {characters}:Characters')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', statusbar_func)

# ----------------------------------- statusbar end --------------------------------


########################### Main menu functionality #######################
# New file functionality
url=''
def new_func(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

# open file  functionality
def openfile_func(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

# Save file  functionality
def save_func(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content1=text_editor.get(1.0,tk.END)
            url.write(content1)
            url.close()
    except:
        return

# Save As file functionality
def saveas_func(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        content=text_editor.get(1.0,tk.END)
        url.write(content)
        url.close()
    except:
        return

def exit_func(event:None):
    global url,text_changed
    try:
        if text_changed:
            message=messagebox.askyesnocancel('warning','Do you want to save this file?')
            if message is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    content1=text_editor.get(1.0,tk.END)
                    url.write(content1)
                    url.close()
            elif message is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return


#binding shortcut keys with their respective functions 
main_app.bind("<Control-n>", new_func)
main_app.bind("<Control-o>", openfile_func)
main_app.bind("<Control-s>", save_func)
main_app.bind("<Control-Alt-s>", saveas_func)
main_app.bind("<Control-q>", exit_func)




# file commands
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_func)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=openfile_func)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_func)
file.add_command(label='Save As',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=saveas_func)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)



# find dialogue box

def find_func():
    def find():
        word=find_input.get()
        text_editor.tag_remove('match',1.0,tk.END)
        match=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                match+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    def replace():
        word=find_input.get()
        replace_word=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_word)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

 # Creating find dialogue  
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find & Replace')
    find_dialogue.resizable(0,0)

    find_frame=ttk.Labelframe(find_dialogue,text='Find & Replace')
    find_frame.pack(pady=40)

    # find and replace labels and inputs
    find_label=ttk.Label(find_frame,text='Find')
    find_label.grid(row=0,column=0,padx=5,pady=5)
    find_input=ttk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=5,pady=5)
    replace_label=ttk.Label(find_frame,text='Replace')
    replace_label.grid(row=1,column=0,padx=5,pady=5)
    replace_input=ttk.Entry(find_frame,width=30)
    replace_input.grid(row=1,column=1,padx=5,pady=5)

    # find and replace btns
    find_btn=ttk.Button(find_frame,text='Find',command=find)
    find_btn.grid(row=2,column=0,padx=8,pady=10)
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace)
    replace_btn.grid(row=2,column=1,padx=8,pady=10)

    find_dialogue.mainloop()


#binding shortcut key with their respective functions 
main_app.bind("<Control-f>", find_func)



# edit commands
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C' ,command=lambda:text_editor.event_generate("<control C>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V' ,command=lambda:text_editor.event_generate("<control V>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<control X>"))
edit.add_command(label='Clear All',image=clearall_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C', command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

# view functionality
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=toolbar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=statusbar_icon, compound=tk.LEFT, command=hide_statusbar)

# color theme commands 
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color) 
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1 


# -------------------------- ending-----------------------------------






main_app.mainloop()
