#Lesson 5 - reading and saving text files

file = open("LoremIpsum.txt", "r") #open and load text from file
print(file.read()) #display text from file
file.close() #close file to free up memory and prevent data corruption (don't worry if you won't close tho)
text = str(input("Type text to save: "))
savefile = open("MyFile.txt", "w") #open or create MyFile.txt for writing data in it
savefile.write(text) #write text to the file
savefile.close() #close the file

#Note: If you type only filename like this, it will read/save file in same folder the program is.
#You can type full path if you want to be specific, like C:\Users\Admin\Documents\File.txt
#Remember that Windows and Unix (Linux, Mac) have different filesystems and index data and hard drives differently.
#For example Windows uses paths like C:\Users\Josh\Desktop\File.jpg or D:\Games\AlienInvasion\savegame.bin
#And Linux uses paths like /usr/home/data/file.png