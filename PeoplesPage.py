from tkinter import *
"""
Creates a list of people that match your description the user entered. This list
shows up after the user presses search in MusicProject
"""
"""
Frame1: Red
Frame2: Orange
OddText Yellow
EvenText: Green
Buttons: Blue
Separator: Purple
"""
#Sorting Method
class PeoplesPageClass():
    def __init__(self):
        root = Tk("People's Page")
        root.title = ("People's Page")
        person1Frame = Frame(root)
        person1Frame.pack()

        nameLabel = Label(person1Frame, text="Justin")
        nameLabel.pack()
        instrumentLabel = Label(person1Frame, text="Flute")
        instrumentLabel.pack()

        areaLabel = Label(person1Frame, text="New York")
        areaLabel.pack()

        musicTypeLabel = Label(person1Frame, text="Classical")
        musicTypeLabel.pack()

        separator = Frame(height=5,bg= "gray", bd=1)
        separator.pack(fill=X, padx=5, pady=5)

        person2Frame = Frame(root)
        person2Frame.pack()

        nameLabel = Label(person2Frame, text="Justin")
        nameLabel.pack()

        instrumentLabel = Label(person2Frame, text="Flute")
        instrumentLabel.pack()

        areaLabel = Label(person2Frame, text="New York")
        areaLabel.pack()

        musicTypeLabel = Label(person2Frame, text="Classical")
        musicTypeLabel.pack()
        root.mainloop()
# PeoplesPageClass()

        #Make fake profiles, with a name, bio, their instrument, where they live, and their
        #type of preffered music to play.