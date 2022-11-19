#Lesson 4 - modules

#as you've probably noticed, you can't really make anything useful with clear basic Python.
#but we can use modules to have more, useful functions!
#there are modules for everything, from displaying random numbers to image editing and advanced AI.
#you download them with terminal command pip install [name]
#in Thonny we can simply click Tools -> Manage Packages and from there search for new modules and install them.
#most common, basic modules are pre-installed
#let's first use one of most basic modules - time
import time  #let's import the module so we can use it
#time module allows our program to wait
print("text")
time.sleep(1)
print("You will see this after a second")
time.sleep(4)
print("And this after next 4")
#as you can see, time can be used to delay events in program
#every module has its own usage, you will find documentation online
#let's import another module - random
import random as loteria #I imported the random module, but as loteria.
#now we will use loteria instead of random when calling this module.
#for this one I didn't have to do that, but if a module had 
#a long or hard name, changing it for your program this way is quite useful.
time.sleep(1) #let's use time again because why not
print("Some random numbers:")
print(loteria.randint(0,100)) #display random number from 0 to 100
print(loteria.randint(0,100))
print(loteria.randint(0,100))
print(loteria.randint(0,100))
print(loteria.randint(0,100))