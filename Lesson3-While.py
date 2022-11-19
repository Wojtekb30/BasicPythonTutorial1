#Lesson 3 - while loop
#sometimes we might want part of program to run many times, or forever. This is when we use while.
#while has similar syntax to if
n=0 #let's create a variable
while n<=10: #this while loop will run if n is smaller or equal to 10
    print(n) #display current value of n
    n=n+1 #add 1 to n
    #this loop will output numbers from 0 to 10.
print("Loop ended")
#if we want our loop to never end, we can use True or a comparison which will always be true (like 1==1)
while True: #this loop will work forever
    t=str(input("Type END to close this loop (but try typing other stuff first): ")) #get input
    if t.lower()=='end': #do something if you typed END
        break #break forces loop to end
    #in this specific scenario the loop works until you type END
print("Loop ended/closed")
#it could be done easier tbh
s=""
while s.lower()!="end":
    s = str(input("Type END to close this loop "))
    
print(":-)")
input("Press ENTER/RETURN to launch the last, eternal loop")
l=0
while 1==1:
    print(l)
    l=l+1
    #you can always press CTRL+C in Shell window to force stop a Python program.
    #or if you use Thonny then press STOP button on top left