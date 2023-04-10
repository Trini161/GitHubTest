#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
def test_my_button():
    frame_auth.tkraise()
    ent_password = tk.Entry(frame_login, show="*", bd=3)
    ent_password.pack(pady=5)
# main window
root = tk.Tk()
root.wm_geometry("400x400")
oldtitle = root.title()
root.title('Authorization')
# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky= 'news' )
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky= 'news')

# Add a label to frame_auth
frame_auth  = tk.Label(frame_login,text="Username")
#create Username
lbl_username = tk.Label(frame_login, text='Username:', font = 'Courier')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
#create Password
lbl_password = tk.Label(frame_login, text='Password:', font = 'Courier')
lbl_password.pack(padx= 50)
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)


#create button
btn_login = tk.Button( frame_login, text='Login', command=test_my_button)  
btn_login.pack()
frame_login.tkraise()
root.mainloop()
# Use get method of ent_password when the button is pressed, and store result
student_password = ent_password.get()
lbl_passwd = tk.Label(frame_login,text="Password")
lbl_passwd.pack(pady=5)
ent_password = tk.Entry(frame_login, show="*", bd=3)
ent_password.pack(pady=5)
# Configure the label in frame_auth to display the password