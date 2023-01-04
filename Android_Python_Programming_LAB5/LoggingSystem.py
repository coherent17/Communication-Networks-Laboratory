import tkinter as tk
from PIL import Image, ImageTk
import pickle

def login(Name, Pwd):

    #get the user input name and password
    entry_usr = Name.get()
    entry_pwd = Pwd.get()

    #check if the user info is in the file compressed in pickle
    try:
        try:
            with open('user_info.pickle', 'rb') as f:
                user_info = pickle.load(f)

    #load error, create a new dict
        except EOFError:
            user_info = {}

    except FileNotFoundError:
        user_info = {}

    #check if user is in the dict load from pickle file
    if entry_usr in user_info:

        #check if the password is correct
        if entry_pwd == user_info[entry_usr]:
            tk.messagebox.showinfo(message = 'Login Sucessfully!')
        else:
            tk.messagebox.showwarning(message = 'Password Error!')

    # if user info not found
    else:
        #create a new account with the entry name & password, return 0/1
        sign_up = tk.messagebox.askyesno(message = 'Do you want to create an account by your input?')
        
        if sign_up:
            with open('user_info.pickle', 'wb') as f:
                user_info = {entry_usr: entry_pwd}
                pickle.dump(user_info, f)
        
        else:
            tk.messagebox.showinfo(message = 'See you!')

#sign up pade back-end
def check_Info(tmpName, tmpPwd, tmpConfirmPwd, w):
    entry_usr = tmpName.get()
    entry_pwd = tmpPwd.get()
    entry_confirm_pwd = tmpConfirmPwd.get()

    try:
        try:
            with open('user_info.pickle', 'rb') as f:
                user_info = pickle.load(f)

        except EOFError:
            user_info = {}

    except FileNotFoundError:
        user_info = {}

    if entry_usr in user_info:
        tk.messagebox.showinfo(message = 'Existed Account!')

    elif entry_pwd != entry_confirm_pwd:
        tk.messagebox.showwarning(message = 'Different Password & Confirm Password!')

    else:
        with open('user_info.pickle', 'wb') as f:
            user_info = {entry_usr: entry_pwd}
            pickle.dump(user_info, f)
            tk.messagebox.showinfo(message = 'Sign Up successfully!')
            w.destroy()

#open a new new side window for user to sign up
def sign_up():
    window2 = tk.Toplevel(window)
    window2.title('Sign Up')
    window2.geometry('275x125')

    tmpName = tk.StringVar()
    tmpName.set('')
    tmpPwd = tk.StringVar()
    tmpPwd.set('')
    tmpConfirmPwd = tk.StringVar()
    tmpConfirmPwd.set('')

    UserName = tk.Label(window2, text = 'User Name').grid(row = 0, column = 0)
    User_Entry = tk.Entry(window2, textvariable = tmpName).grid(row = 0, column = 1)
    Password = tk.Label(window2, text= 'Password').grid(row = 1, column = 0)
    Password_Entry = tk.Entry(window2, textvariable = tmpPwd, show = '*').grid(row = 1, column = 1)
    Confirm_Password = tk.Label(window2, text= 'Confirm Password').grid(row = 2, column = 0)
    Confirm_Password_Entry = tk.Entry(window2, textvariable = tmpConfirmPwd, show = '*').grid(row = 2, column = 1)
    Sign_UP_Btn = tk.Button(window2, text = 'Sign up', borderwidth = 5, width = 8, height = 1, command = lambda: check_Info(tmpName, tmpPwd, tmpConfirmPwd, window2)).grid(row = 3, column = 1)

#main driven code
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Lab5")
    window.geometry('300x400')

    f1 = tk.Frame(window)
    f2 = tk.Frame(window)
    f1.pack()
    f2.pack()

    #Put the image on the upper frame
    image1 = ImageTk.PhotoImage(Image.open('CoffeeShop.jpg'). resize((300,200)))
    im = tk.Label(f1, image=image1)
    im.pack()


    Name = tk.StringVar()
    Name.set('')
    Pwd = tk.StringVar()
    Pwd.set('')

    User = tk.Label(f2, text = 'User:').grid(row = 0, column = 0)
    User_Entry = tk.Entry(f2, textvariable = Name).grid(row = 0, column = 1)
    Password = tk.Label(f2, text= 'Password:').grid(row = 1, column = 0)
    Password_Entry = tk.Entry(f2, textvariable = Pwd, show = '*').grid(row = 1, column = 1)
    login_btn = tk.Button(f2, text = 'Login', borderwidth = 5, width = 8, height = 1, command = lambda: login(Name, Pwd)).grid(row = 4, column = 0)
    sign_btn = tk.Button(f2, text = 'Sign up', borderwidth = 5, width = 8, height = 1, command = lambda: sign_up()).grid(row = 4, column = 1)

    window.mainloop()