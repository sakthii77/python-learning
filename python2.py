
#for loop

#Example:

place= "india"
for g in place:
    print(g)

#Range:

#Example:

for g in range (0,10,2):
    print(g)

#Small Programs By using For and Range :

#Addition of Numbers by Given Range:

i=int(input("Enter the number range :"))
total=0
for g in range (0,i+1):
    total+=g
else:
    print("The total of given number rang is :",total)

#Multiple Of Numbers by Given Range:
i=int(input("Enter the number range :"))
total=1
for g in range (1,i+1):
    total*=g
else:
    print("The Multiple of given number rang is :",total)

#No.of Words in a Given String:
i=input("Enter the Word :")
total=1
for g in i:
    if g==" ":
        total=total+1
else:
    print("no.of words in given string ",total)

#No.of Sentences in a Given String:
i=input("Enter the sentences :")
total=1
for g in i:
    if g==("." and " "):
        total=total+1
else:
    print("no.of sentences in given string :",total)


#find prime or not By Using For Loop:

no=int(input("Enter the Number :"))
if no>2:
    for i in range (2,no):
        if no%i==0:
            print("This is not a prime number")
        break
else:
    print("This is a prime number")
if no==0 and no==1:
    print("This is not a prime number")
elif no==2:
    print("This is a prime number")

#Find The Total Characters in Given String:

let=input("Enter the Sentences :")
count=0
for gp in let:
    if gp!=" ":
        count=count+1
    print(count)

#To Find No.of Letters and Special Characters and Numbers in Given Input:
let=input("Enter the Sentences :")
al=sp=0
nu=0
for gp in range(len(let)):
    if let[gp]>="a" and let[gp]<="z":

        al=al+1

    elif  let[gp]>="0" and let[gp]<="9":
        nu=nu+1
else:
    if let[gp]!=" ":
        sp=sp+1
    else:
        print("no.of alphabets :",al)
        print("no.of special characters :", sp)
        print("no.of Numbers :", nu)