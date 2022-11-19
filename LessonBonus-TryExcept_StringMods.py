#Bonus lesson (3.5) - try&except, string modification

#Normally, if something goes wrong the program crashes. For example if you try to divide by 0
print("Let's divide 2 numbers!")
numerouno=int(input('Type first number (a): '))
numerodos=int(input('Type second number (a): '))
print(numerouno/numerodos)
#as you can see, if you type letters not numbers or 0 as the second number, the program crashes.
#after all it's impossible to do math on text or divide by 0.
#now let's try again, but this time use Try and Except
#let's put all of this in a loop first, because why not:
print('checkpoint')
NewNumeroUno=0
NewNumeroDos=0
while True:
    NewNumeroUno =input('Type first number (b): ') #I can remove conversion to numbers from input
    NewNumeroDos=input('Type second number (b): ')
    try: #try runs first
        print(float(NewNumeroUno)/float(NewNumeroDos)) #convert to numbers and divide
        NewNumeroUno=0 #let's reset the variables
        NewNumeroDos=0
    except: #if something in try fails, stuff in except runs
        
        if NewNumeroUno.lower()=='end' or NewNumeroDos.lower()=='end':
            print("loop closed")
            break #way for you to close this loop and go further (type end)
        print("Error! Try different numbers")
        NewNumeroUno=0
        NewNumeroDos=0
#now if the calculations fail, the program will display the error message and still work instead of crashing

#String modifications
#Here I will show you how to make a String shorter or get specific part of it
word = str(input("Type text: "))
word = word[1:] #this way you can remove X letters from a word
print(word) #display the word but now without the first letter
slowo = str(input("Type some longer text: "))
digit = int(input("How many first letters remove?: "))
print(slowo[digit:]) #display the word but now without 'digit' amount of letters
palabra = str(input("Type some longer text again: "))
liczba = int(input("Which letter from this word should I display?: "))
print(palabra[liczba]) #display 'liczba' letter from the string.
#remember that in computer science array starts at 0
liczba = int(input("Which letter from this word should I display again?: "))
print(palabra[liczba-1]) #but if we do this, we can type the index number like if the array started at 1

