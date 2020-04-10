import tkinter as tk
from tkinter import *
import smtplib
def clicked():
    mail()
def mail():
    import python_proj
   
    
root=tk.Tk()
    
canvas=tk.Canvas(root,height=300,width=400)
canvas.pack()

frame=tk.Frame(root,bg='#80c1ff',bd=10)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.4,anchor='n')

label=tk.Label(frame,text="WELCOME",padx=20, fg = "red",font = "Times")
label.pack()

radio=tk.Radiobutton(frame, text="MAIL",value=1,fg="red",command=lambda: clicked())
radio.place(relx=0.2,rely=0.3,relwidth=0.25)

radio=tk.Radiobutton(frame, text="TEXT",padx = 20,value=2,fg="red")
radio.place(relx=0.5,rely=0.3)

root.mainloop()
