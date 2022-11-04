# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:19:50 2022

@author: BAMBI
"""

from tkinter import*
import random

root = Tk()
root.title("Random colour")
root.geometry("500x500")

dictonary = {'colors': ['maroon1','lawn green','magenta1','purple1','springgreen2','chocolate', 'deep pink','cyan','darkslategray1','turquoise1','hotpink1','lightseagreen','orchid1','hotpink4','thistle3']}

def pick():
    
    random_no = random.randint(0,14)
    colour_no = dictonary["colors"][random_no]
    print(colour_no)
    root.configure(background=colour_no)
    
btn = Button(root,text="Click Me",command=pick,bg="white",fg="gray")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()