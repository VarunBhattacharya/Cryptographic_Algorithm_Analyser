#####################################################################################
############################## Import libraries #####################################
#####################################################################################
from ctypes import alignment
from pydoc import text
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
# from pyautogui import confirm #window shrink problem
import os
from os import system
from pyglet import font
import datetime
font.add_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts/Ubuntu_Mono_Bold_Italic.ttf"))

# from mainPage import log
from algo.modEncAlgo.aesCipher import *
from algo.modEncAlgo.desCipher import *

#####################################################################################
############################## Create Instance ######################################
#####################################################################################
window = Tk()

#####################################################################################
############################## Window Params ########################################
#####################################################################################
window.geometry("1270x720")
window.resizable(False, False)
window.title("Modern Encryption Techniques")

#####################################################################################
############################## Algorithmic Functions ################################
#####################################################################################
def log(text):
    with open('log.txt','a') as f:
            f.write(f"{datetime.datetime.now()}: {text}\n")

def encrypt():
    if userInput.get("1.0",'end-1c') == "Enter text here" or userInput.get("1.0",'end-1c') == "":
        messagebox.showerror(title = "Invalid Input", message = "Please enter text to encrypt or decrypt")
    elif algoCombo.get() == "":
        messagebox.showerror(title = "Invalid Input", message = "Please select an algorithm")
    else:
        log(f"{algoCombo.get()} Modern Encryption Selected")
        print(f"{algoCombo.get()} Modern Encryption Selected")

        if algoCombo.get() == "DES":
            inp = userInput.get("1.0",'end-1c')
            startTime = time.perf_counter_ns()
            obj = desCipher(inp)
            result = obj.encryptMessage()
            endTime = time.perf_counter_ns()
            textOutput.delete('1.0', END)
            result2 = f"\n\n\nTime taken for execution is: {str(round(endTime-startTime, 7))} nanoseconds."
            textOutput.insert(tk.END, result)
            textOutput.insert(tk.END, result2)
        
        if algoCombo.get() == "AES":
            inp = userInput.get("1.0",'end-1c')
            startTime = time.perf_counter_ns()
            obj = aesCipher(inp)
            result = obj.encryptMessage()
            endTime = time.perf_counter_ns()
            textOutput.delete('1.0', END)
            result2 = f"\n\n\nTime taken for execution is: {str(round(endTime-startTime, 7))} nanoseconds."
            textOutput.insert(tk.END, result)
            textOutput.insert(tk.END, result2)

def decrypt():
    if algoCombo.get() == "":
        messagebox.showerror(title = "Invalid Input", message = "Please select an algorithm")
    else:
        log(f"{algoCombo.get()} Modern Decryption Selected")
        print(f"{algoCombo.get()} Modern Decryption Selected")

        if algoCombo.get() == "DES":
            inp = userInput.get("1.0",'end-1c')
            startTime = time.perf_counter_ns()
            obj = desCipher(inp)
            result = obj.decryptMessage()
            endTime = time.perf_counter_ns()
            textOutput.delete('1.0', END)
            result2 = f"\n\n\nTime taken for execution is: {str(round(endTime-startTime, 7))} nanoseconds."
            textOutput.insert(tk.END, result)
            textOutput.insert(tk.END, result2)

        if algoCombo.get() == "AES":
            inp = userInput.get("1.0",'end-1c')
            startTime = time.perf_counter_ns()
            obj = aesCipher(inp)
            result = obj.decryptMessage()
            endTime = time.perf_counter_ns()
            textOutput.delete('1.0', END)
            result2 = f"\n\n\nTime taken for execution is: {str(round(endTime-startTime, 7))} nanoseconds."
            textOutput.insert(tk.END, result)
            textOutput.insert(tk.END, result2)

def back():
    # choice = confirm("Proceed?", buttons=["Ok"])
    log("Returned to Main Page")
    print("Returned to Main Page")
    window.destroy()
    system('python -u "mainPage.py"')

#####################################################################################
############################## Create Canvas ########################################
#####################################################################################
canvas = Canvas(window)

#####################################################################################
############################## Background Image #####################################
#####################################################################################
fname = PhotoImage(file = "assets/modEncAlgoBg.png")
bgLabel = Label(window, image = fname)
bgLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#####################################################################################
############################## Window Structure #####################################
#####################################################################################
frame = Frame(window)

#Back Button
backButton = Button(window, text = "<", font = ("Ubuntu_Mono_Bold_Italic bold", 13), fg = "white",
    height = 2, width = 7, bg = "#381044", command = lambda: back(), cursor = "exchange"
    )
backButton.place(x = 0, y = 0)

#User Input Text Area
userInput = Text(window, height = 9, width = 133, bg = "#381044", borderwidth = 0, 
    fg = "white", padx = 2, pady = 2, cursor = "spider"
)
userInput.place(x = 98, y = 108)
userInput.insert('end', "Enter text here")
userInput.config(font = "Ubuntu_Mono_Bold_Italic 11 bold")

#Output Text Area
textOutput = Text(window, height = 9, width = 133, bg = "#381044", borderwidth = 0, 
    fg = "white", padx = 2, pady = 2, cursor = "spider"
    )
textOutput.place(x = 98, y = 508)
textOutput.config(font = "Ubuntu_Mono_Bold_Italic 11 bold")

#Encrypt Button
encryptButton = Button(window, text = "Encrypt", font = "Ubuntu_Mono_Bold_Italic 9 bold", fg = "white",
    height = 3, width = 30, bg = "#381044", command = lambda: encrypt(), cursor = "pirate"
    )
encryptButton.place(x = 671, y = 379)

#Decrypt Button
decryptButton = Button(window, text = "Decrypt", font = "Ubuntu_Mono_Bold_Italic 9 bold", fg = "white",
    height = 3, width = 30, bg = "#381044", command = lambda: decrypt(), cursor = "pirate"
    )
decryptButton.place(x = 911, y = 379)

#ComboBox Configure
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#381044',
                                       'fieldbackground': '#381044',
                                       'background': 'white',
                                       'borderwidth': 10,
                                       }}}
                         )
combostyle.theme_use('combostyle') 

#ComboBox Selection
algoChoose = tk.StringVar()
algoCombo = ttk.Combobox(window, width = 29, 
    textvariable = algoChoose, state = 'readonly', font = "Ubuntu_Mono_Bold_Italic 15 bold", cursor = "spraycan"
    )
algoCombo['values'] = ('DES', 'AES')
algoCombo.place(x = 180, y = 392)

#####################################################################################
############################## Main Loop ############################################
#####################################################################################
canvas.pack()
window.mainloop()