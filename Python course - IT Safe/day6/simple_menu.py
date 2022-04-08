from tkinter import Tk, Menu


def window_exit():
   window.destroy()

window = Tk()
window.title('My Title')
window.geometry("500x500")
window.iconbitmap('app.ico')
window.resizable(False, False)

menu = Menu(window)
new_item = Menu(menu)

new_item.add_command(label='New')
new_item.add_command(label='Save')
new_item.add_separator()
new_item.add_command(label='Exit', command = window_exit)


menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()