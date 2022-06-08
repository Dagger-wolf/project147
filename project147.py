# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:56:03 2022

@author: aarya_fhxkeec
"""

from tkinter import*
root = Tk()
root.title("ASCII Encryption")
root.geometry("800x600")
root.configure(background="purple")

enter_word = Entry(root)

label = Label(root, text="Name in ASCII: ")
label_encrypt = Label(root, text="Encrypted in ASCII: ")

def convert_to_ascii() :
    inputg = enter_word.get()
    
    for letter in inputg :
        label["text"] = label["text"] + "  " +str(ord(letter)) + "  "
        
        encrypted = int(ord(letter))
        del_1_encrypt = encrypted-1
        label_encrypt["text"] = label_encrypt["text"] + str(chr(del_1_encrypt))
        
        
        
btn = Button(root, text="Show Name In ASCII And Encrypt It", command=convert_to_ascii)

enter_word.place(relx=0.5, rely=0.3, anchor=CENTER)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label_encrypt.place(relx=0.5, rely=0.6, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()