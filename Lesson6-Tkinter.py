#Lesson 6 - Tkinter

#Tkinter is a module which allows you to create a graphical user interface for your program.
#After all it's not early 90's anymore, we have operating systems with desktop like Windows.
#You can't really expect others to use a terminal app nowadays.
#Last thing is that it's simply not possible to do some stuff in terminal.

global n #a global variable for later. Global variables work everywhere in the program.
n=0

def addone(): #define function which adds 1 to n and render label again
    global n
    global label
    n=n+1
    label.destroy()
    label = tk.Label(text=n)
    label.pack()
def minusone(): #define function which substracts 1 from n and renders label again
    global n
    global label
    n=n-1
    label.destroy()
    label = tk.Label(text=n)
    label.pack()

import tkinter as tk #import tkinter, I do it under name tk because it's easier to type
root = tk.Tk() #create a window. You can call it however you want, but most programmers name it root
root.title("My program") #set window title
root.geometry('700x500') #set size of window

global label #make label global

label = tk.Label(text=n) #create a label - element that displays text


buttonadd = tk.Button(root, text="+1", command=addone) #create +1 button
buttonadd.pack() #render it
buttonminus = tk.Button(root, text="-1", command=minusone, background='red', foreground='white') #create red -1 button
buttonminus.pack() #render it
#the buttons now run stuff in their functions - addone or minusone. We defined them before, in lines 11 and 18.
label.pack() #render the prevously added label in window
#tkinter has lot of more to offer, but you can read about that in their documentation and then use it properly.
root.mainloop() #loop of the window, you must add it to make it work


