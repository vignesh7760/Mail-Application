from tkinter import *
import smtplib

# Functions 
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username =="" or password =="" or to =="" or subject =="" or body=="" :
            notif.config(Text ='All files are required', fg ='red' )
            return
        else:
            finalMessage = 'sunject: {}\n\n{}'.format(subject,body)
            server = smtplib.SMTP('smpt.gmail.com', 587)
            server.starttls()
            server.login(username,password)
            server.sendmail(username,to,finalMessage)
            notif.config(Text= "Email has been successfully sent" , fg="green")
    except: 
        notif.config(Text="Error sending mail" , fg="red")

def reset():
    usernmaaeEntry.delete(0 , 'end')
    passwordEntry.delete(0 , 'end')
    receiverEntry.delete(0 , 'end')
    subjectEntry.delete(0 , 'end')
    BodyEntry.delete(0 , 'end')
  

# Main Screen
root = Tk()
root.title("Email")
root.geometry("550x350")
root.resizable(0 ,0)



# Graphice
Label(root , text= "Custom Email App", font=('calibri', 15)).grid(row=0 , sticky= N)
Label(root , text= "Use the form below to send the mail", font=('calibri', 15)).grid(row=1 ,sticky=W, padx=5)
Label(root , text= "EMAIL :", font=('calibri', 15)).grid(row=2 ,sticky=W, padx=5 )
Label(root , text= "Password :", font=('calibri', 15)).grid(row=3 ,sticky=W, padx=5)
Label(root , text= "To :", font=('calibri', 15)).grid(row=4 ,sticky=W, padx=5)
Label(root , text= "Subject: ", font=('calibri', 15)).grid(row=5 ,sticky=W, padx=5)
Label(root , text= "Body : ", font=('calibri', 15)).grid(row=6 ,sticky=W, padx=5)
notif = Label(root , text= "", font=('calibri', 15))
notif.grid(row=7 ,sticky=W, padx=5)

# Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()
 
# Entries
usernmaaeEntry = Entry(root, textvariable=temp_username)
usernmaaeEntry.grid(row=2 , column= 1)
passwordEntry = Entry(root, show= "*" , textvariable=temp_password)
passwordEntry.grid(row=3  , column= 1)
receiverEntry = Entry(root, textvariable=temp_receiver)
receiverEntry.grid(row=4 , column= 1)  
subjectEntry = Entry(root, textvariable=temp_subject)
subjectEntry.grid(row=5, column= 1)  
BodyEntry = Entry(root, textvariable=temp_body)
BodyEntry.grid(row=6, column= 1)  

# Buttons
Button(root , text="Send", command=send).grid(row=7 , column=0)
Button(root , text="Rset", command=reset).grid(row=7 ,column= 1)

  

root.mainloop()