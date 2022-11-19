#Lesson 2 - if

#if is used to check if a condition is satisfied or not
#First, let's make a input variable
variable = int(input("Type number: "))
#now let's check if it equals something specific, for example 5:
if variable == 5:
    print("This will be displayed if you typed 5")
else:
    print("And this if you typed something else. Else argument is optional")
#as you can see, indents were used to mark the print is inside if
if variable == 6:
    print("This is inside the if")
    print("This too")
print("but this is not")
#now let's see if the typed number is bigger than 7
if variable > 7:
    print("You typed number bigger than 7.")

#logic comparators:
# == checks if both variables or values are equal
# != checks if they are different
# < and > let you check is something is bigger/smaller
# <= and >= are bigger/smaller or equal to
if variable >=12:
    print("You typed something bigger or equal to 12")
# you can also check if multiple conditions are met. Let's add a second input first
zmienna = int(input("Type second number: "))
if zmienna == 10 and variable == 15:
    print("This will run only if both conditions are true")
if zmienna == 19 or variable == 20:
    print("This will run if either conditions are true")
    #in this case if zmienna is equal to 19 or variable to 20, or both
#you can also compare text
text = str(input("Now type text: "))
if text == "Hello":
    print("Hi (answering Hello)")
else:
    print("You didn't type 'Hello'")
#you can also convert text to uppercase or lowercase, so you don't have to care how people will type
print(text.upper()) #convert to uppercase
print(text.lower()) #convert to lowercase
if text.lower() == "hi":
    print("Hello (answering hi)")


