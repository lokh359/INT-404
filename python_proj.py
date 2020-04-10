import tkinter as tk
import smtplib
def get_mail(t,content):
    try:
        
        mail=smtplib.SMTP('smtp.gmail.com:587')
        mail.ehlo()
        mail.starttls()
        mail.login("ur mail","paswd")
        mail.sendmail("ur mail",str(t),content)
        mail.close()
        print("Mail sent")
    except:
        print("Failed to sent")

root=tk.Tk()
canvas=tk.Canvas(root,height=500,width=600)
canvas.pack()

frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

entry1 = tk.Entry(lower_frame,font=40)
entry1.place(relwidth=1, relheight=1)

button=tk.Button(frame,text="mail",command=lambda: get_mail(entry.get(),entry1.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)




root.mainloop()
