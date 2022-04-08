from tkinter import messagebox, Tk, Button, Entry, Label, Text, END

def btn1_func():
   command = ent1.get()
   txt1.delete("1.0", "end")
   txt1.insert(END, command)

window = Tk()
window.title('My Title')
window.geometry("300x300")
window.iconbitmap('app.ico')
window.resizable(False, False)

lbl1 = Label(window, text = "User Name")
lbl1.place(x = 0,y = 5)
ent1 = Entry(window, width = 20)
ent1.place(x = 80,y = 5)
btn1 = Button(window, text = "execute", command = btn1_func)
btn1.place(x = 220,y = 0)

txt1=Text(window)
txt1.place(x=0, y=50)

window.mainloop()
