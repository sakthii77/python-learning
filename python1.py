#While Loop
#Examples:
i=0
while i<=100:
    i+=1
    if i%3==0 and i%2==0:
        print(i)
else:
    print(i,"not divided by 2 & 3")

#Addition of first n numbers
total=0
numbers=1
while numbers<=5:
    total=total+numbers
    numbers += 1
print(total)

#Multiply of first n numbers

total=1
numbers=2
while numbers<=5:
    total=total*numbers
    numbers += 1
print(total)

#Loop

name=input("Enter your name")
i=0
while i<len(name):
    print(name[i])
    i+=1

#Break and continue:
no=1
while no<=10:
    if no==5:
        no+=1
        continue
    print(no)
    no+=1


no=1
while no<=10:
    if no==5:
        break
    print(no)
    no+=1

#Guess the Random value:
from random import randint

system_mind=randint(10,20)

while True:
    person=int(input("enter your guess"))
    if system_mind==person:
        print("your guess is correct")
    elif system_mind<person:
        print("your guess is greater than ")
    else:
        print("your guess is low")