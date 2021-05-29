from tkinter import *
import tkinter as tk
import sqlite3
conn = sqlite3.connect('C:\\Users\\15164\\Downloads\\music_db.sqlite')
cursor = conn.cursor()


class WelcomePageClass:

    def __init__(self):
        root = tk.Tk()
        root.title = "Welcome Page"
        # Creates a label saying "Welcome" and adds it to the frame.
        WelcomeLabel = Label(root, text="Welcome:")
        WelcomeLabel.pack()

        nameLabel = Label(root, text="Enter your name:")
        nameLabel.pack()
        self.name = tk.Entry(root)
        self.name.pack()

        countryLabel = Label(root, text="Enter your country of residence:")
        countryLabel.pack()
        self.country = tk.Entry(root)
        self.country.pack()

        stateLabel = Label(root, text="Enter your state (If applicable):")
        stateLabel.pack()
        self.state = tk.Entry(root)
        self.state.pack()

        instrumentLabel = Label(root, text="What instrument(s) do you play? (Separate by space)")
        instrumentLabel.pack()
        self.instrument = tk.Entry(root)
        self.instrument.pack()

        accompanyLabel = Label(root, text="What instrument(s) do you play with? (Separate by space)")
        accompanyLabel.pack()
        self.accompany = tk.Entry(root)
        self.accompany.pack()

        musicTypeLabel = Label(root, text="What music genre(s) do you play? (Separate by space)")
        musicTypeLabel.pack()
        self.musicType = tk.Entry(root)
        self.musicType.pack()

        zipcodeLabel = Label(root, text="Enter your zipcode:")
        zipcodeLabel.pack()
        self.zipcode = tk.Entry(root)
        self.zipcode.pack()

        bioLabel = Label(root, text="Enter your bio (This can be left blank):")
        bioLabel.pack()
        self.bio = tk.Entry(root)
        self.bio.pack()

        signUpButton = Button(master=root, text="SignUp", command=lambda: self.callback(root))
        signUpButton.pack()

        root.mainloop()

    # def callback(self, curr_page):
    #     print("Hi I'm in the callback")
    #     # curr_page.destroy()
    #     PeoplesPageClass()
    def callback(self, root):
        userInfo = (self.name.get(), self.country.get(), self.state.get(), self.instrument.get(), self.accompany.get(),
                    self.musicType.get(), self.zipcode.get(), self.bio.get())
        self.enterData(record=userInfo)
        root.destroy()
        from Matching import MatchingClass
        MatchingClass()

    def enterData(self, record):
        insert_query = """
        INSERT INTO Musician 
                ( 
                            name,
                            country, 
                            state, 
                            instrument,
                            accompany,
                            musicType, 
                            zipcode, 
                            biography 
                ) 
                VALUES 
                ( 
                            '{}','{}','{}','{}','{}','{}', {}, '{}'
                );""".format(*record)

        cursor.execute(insert_query)
        conn.commit()


WelcomePageClass()



# https://www.delftstack.com/howto/python-tkinter/how-to-switch-frames-in-tkinter/
# Switching frames
# https://pythonprogramming.net/change-show-new-frame-tkinter/
"""
Python Events
https://pythonprogramming.net/tkinter-tutorial-python-3-event-handling/
"""
