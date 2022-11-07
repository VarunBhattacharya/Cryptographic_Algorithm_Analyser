# import tkinter as tk

# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()

#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)

# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()

#     def close_windows(self):
#         self.master.destroy()

# def main(): 
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()

# if __name__ == '__main__':
#     main()





from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('200x200')


pytroop = StringVar()
pytroop.set("Blue")



def print(ans):
    Label(window , text = ans).pack()

Radiobutton(window , text = "Blue" , variable = pytroop , value = "Blue" ).pack()
Radiobutton(window , text = "Green" , variable = pytroop , value = "Green" ).pack()
Radiobutton(window , text = "Red" , variable = pytroop , value = "Red" ).pack()

a = Button(window , text = "select" , command = lambda : print(pytroop.get())).pack()


window.mainloop()