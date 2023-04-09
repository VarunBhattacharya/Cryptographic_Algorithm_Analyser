#####################################################################################
############################## Import libraries #####################################
#####################################################################################
from ctypes import alignment
from pydoc import text
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# from pyautogui import confirm #window shrink problem
import os
from os import system
from pyglet import font
import datetime
font.add_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts/Ubuntu_Mono_Bold_Italic.ttf"))



#####################################################################################
############################## Create Instance ######################################
#####################################################################################
window = Tk()



#####################################################################################
############################## Window Params ########################################
#####################################################################################
window.geometry("1270x720")
window.resizable(False, False)
window.title("Cryptographic Algorithms Analyser")



#####################################################################################
############################## Algorithmic Functions ################################
#####################################################################################
def log(text):
    with open('log.txt','a') as f:
            f.write(f"{datetime.datetime.now()}: {text}\n")

def substAlgo():
    log("Substitution Algorithm Selected")
    print("Substitution Algorithm Selected")
    window.destroy()
    system('python -u "substAlgoPg.py"')

def transAlgo():
    log("Transposition Algorithm Selected")
    print("Transposition Algorithm Selected")
    window.destroy()
    system('python -u "transAlgoPg.py"')

def modEncAlgo():
    log("Modern Encryption Algorithm Selected")
    print("Modern Encryption Algorithm Selected")
    window.destroy()
    system('python -u "modEncAlgoPg.py"')

def assymmetricEncAlgo():
    log("Asymmetric Encryption Algorithm Selected")
    print("Asymmetric Encryption Algorithm Selected")
    window.destroy()
    system('python -u "assymmetricEncAlgoPg.py"')

#####################################################################################
############################## Create Canvas ########################################
#####################################################################################
canvas = Canvas(window)



#####################################################################################
############################## Background Image #####################################
#####################################################################################
fname = PhotoImage(file = "assets/MainPage.png")
bgLabel = Label(window, image = fname)
bgLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)



#####################################################################################
############################## Window Structure #####################################
#####################################################################################
'''Substitution Algorithm'''
substButton = Button(window, text = "Substitution Algorithms", 
    font = "Ubuntu_Mono_Bold_Italic 12 bold italic", fg = "white",
    height = 3, width = 30, bg = "#1F33E2", command = lambda: substAlgo(), cursor = "pirate"
    )
substButton.place(x = 103, y = 276)

'''Transposition Algorithm'''
transButton = Button(window, text = "Transposition Algorithms", 
    font = "Ubuntu_Mono_Bold_Italic 12 bold italic", fg = "white",
    height = 3, width = 30, bg = "#1F33E2", command = lambda: transAlgo(), cursor = "pirate"
    )
transButton.place(x = 103, y = 376)

'''Modern Encryption Algorithm'''
modEncButton = Button(window, text = "Modern Encryption Algorithms", 
    font = "Ubuntu_Mono_Bold_Italic 12 bold italic", fg = "white",
    height = 3, width = 30, bg = "#1F33E2", command = lambda: modEncAlgo(), cursor = "pirate"
    )
modEncButton.place(x = 103, y = 476)

'''Assymmetric Encryption Algorithm'''
assEncButton = Button(window, text = "Assymmetric Encryption Algorithms", 
    font = "Ubuntu_Mono_Bold_Italic 12 bold italic", fg = "white",
    height = 3, width = 30, bg = "#1F33E2", command = lambda: assymmetricEncAlgo(), cursor = "pirate"
    )
assEncButton.place(x = 103, y = 576)



#####################################################################################
############################## Main Loop ############################################
#####################################################################################
canvas.pack()
window.mainloop()