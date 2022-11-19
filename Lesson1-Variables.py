#Variables

#this is how a comment looks like. Comments are not executed.
variable = "Hi" #a string (text) variable
lastpart = " how are you?" #another variable
numerouno = 1 #number (integrer) variable
numerodos = 2 #and another one
numerotres = 3.987654321 #a float
print("Hello world") #print displays output.
#You can print a variable, number or words (if you write them in "")
print(variable + lastpart) #You can add variables of the same type.
#Adding strings results in them getting joined together
print(numerouno + numerodos) #adding numbers adds them like numbers
print(numerouno - numerodos) #other math operations work too
print(numerodos+numerotres) #adding a int and float
print(variable + str(numerodos)) #you must convert variables to the same type before joining them
#int is integrers, full numbers like 1, 7, 666 etc.
#str are strings - text
#floats are numbers like 3.14
#for obvious reasons you can't convert text to numbers (unless there are only numbers in a string)
yourname = input("Type your name: ") #input allows user to type something
print("Hello "+yourname)