import tkinter as tk
from tkinter import filedialog
import os

#No commant in you want to insert manual path 
#path = input("Enter path: ")

#No comment if you want to change default phrase
#phrase = input("Enter phrase: ")
phrase = "tua evidenziazione"


#This open up file finder
root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename()


#Open file in python and read it
with  open(path, encoding="mbcs") as f:
    lines = f.readlines()


#Delete full line if there is in that line the phrase
with open(path, 'w', encoding="mbcs") as f:
    for line in lines:
        if line.strip("\n").find(phrase) == -1 :
            f.write(line)
