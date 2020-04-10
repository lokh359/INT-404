import tkinter as tk
import requests
import json
def get_sms(t,content):
    
    

    URL = 'https://www.way2sms.com/api/v1/sendCampaign'

  
    req_params = {
      'apikey':apiKey,
      'secret':secretKey,
      'usetype':useType,
      'phone': t,
      'message':content,
      'senderid':senderId
      }
      
  
    return requests.post(reqUrl, req_params)


"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
#print (response.text)


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

button=tk.Button(frame,text="sms",command=lambda: get_sms(entry.get(),entry1.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)




root.mainloop()
