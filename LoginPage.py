"""
Login Page:
Username Textbox *
Password Textbox
Log in Button *
Sign up Button

First Screen:
Welcome Text
Search Button
Specifier Menu

Peoples Page:
Basic Information Box
Message Button
Specific Information Button
Back Button

Specific Person Page:
Bio Text
Message Button
Back Button
"""
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

class LoginPageClass:

    def __init__(self):
        root = tk.Tk()
        root.title = "Welcome Page"
        # Creates a label saying "Welcome" and adds it to the frame.
        WelcomeLabel = Label(root, text="Welcome:")
        WelcomeLabel.pack()

        nameLabel = Label(root, text="Enter your username:")
        nameLabel.pack()
        self.username = tk.Entry(root)
        self.username.pack()

        passwordLabel = Label(root, text="Enter your password:")
        passwordLabel.pack()
        self.password = tk.Entry(root)
        self.password.pack()

        loginButton = Button(master=root, text="Log in", command=lambda: self.callback(root))
        loginButton.pack()

        signUpButton = Button(master=root, text="Sign up?", command=lambda: self.callback(root))
        signUpButton.pack()

        root.mainloop()

    def callback(self, root):
        userInfo = (self.username.get(), self.password.get())
        # self.enterData(record=userInfo)
        root.destroy()
        from WelcomePage import WelcomePageClass
        WelcomePageClass()


LoginPageClass()

# passwordEntry.pack()
# def checkValidUserPass():
#     userStr = userNameVar.get()
#     passwordEnteredStr = passwordVar.get()
#     var = StringVar()
#     var.set("Your username or password is incorrect.")
# #Username: Justin Password: Vivobook
#     if userStr != "Justin" or passwordEnteredStr != "Vivobook":
#         messagebox.showerror("Error", "Incorrect username or password")
#         # popup = Message(textvariable=var, relief=RAISED)
#         # popup.pack()
#
# b = Button(root,text='Login',command=checkValidUserPass)
# b.pack()
#
# signUpButton = Button(root,text='Sign Up?',command=checkValidUserPass)
# signUpButton.pack()
#
# root.mainloop()