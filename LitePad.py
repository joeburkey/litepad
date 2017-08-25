import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
 
root = Tkinter.Tk(className="NotePad X")
notePad = ScrolledText(root, width=100,height=200)
 
# define functions for each menu item to use later
 
def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            notePad.insert('1.0',contents)
            file.close()
 
def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = self.notePad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
         
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
 
def about_command():
    label = tkMessageBox.showinfo("About", " NotePad X \n Created by Joseph Burkey \n Version 1.0 \n All rights reserved")

#create menus and implement each defined function
mainMenu = Menu(root) #creates the window and applies the tk widget to said window

root.configure(menu = mainMenu)

subMenu = Menu(mainMenu)


mainMenu.add_cascade(label="File",menu=subMenu)

mainMenu.add_command(label="About",command=about_command)

subMenu.add_command(label="Open",command=open_command)

subMenu.add_command(label="Save",command=save_command)

subMenu.add_command(label="Exit",command=exit_command)



#subMenu.add_cascade(label="New File", command = create_window)

#create keybindings for shortcuts - release in version 1.1

#
notePad.pack()
root.mainloop()
