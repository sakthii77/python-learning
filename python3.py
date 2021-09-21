
#Pattern Program by using Loops:

#While Loop:

#ex:1

no_of_times=1
value=1
while no_of_times<=5:
    print(value,end=" ")
    no_of_times+=1
    value+=1

#ex:2

value=1
while value<=5:
    no_of_times=1
    while no_of_times<=5:
        print(value,end=" ")
        no_of_times+=1
    print()
    value+=1



#Input From User MAX.Row and MAX.col:

max_row=int(input("Enter the row limit"))
max_col=int(input("Enter the col limit"))
row=1
while row<= max_row:
    col=1
    while col<=max_col:
        print(col,end=" ")
        col+=1
    print()
    row+=1
   

#Addition of Col & Row:

max_row=int(input("Enter the row limit"))
max_col=int(input("Enter the col limit"))
row=1
while row<= max_row:
    col=0
    while col<=max_col:
        print(col+row,end=" ")
        col+=1
    print()
    row+=1
 

#Ex:

row=1
while row<=5:
    col=1
    while col<=row:
        print(row,end=" ")
        col+=1
    print()
    row+=1
   


#Ex:2

row=1
value=5
while row<=5:
    col=1
    while col<=value:
        print(col,end=" ")
        col+=1
    print()
    row+=1
    value-=1

#Printing * with number
row=5
while row<=5:
    if row<1:
        break
    col=1
    while col<=row:
        print(col,end=" ")
        col+=1
        print("*",end="")
    print()
    row-=1

#2
row=5
while row>=1:
    col=1
    while col<row:
        print(col,end=" ")
        col+=1
    col_star=1
    while col_star<=5-row:
        print("*",end=" ")
        col_star+=1
    print()
    row-=1
  
#3

row=5
while row>=1:
    col=1
    while col<row:
        print(" ",end=" ")
        col+=1
    col_star=1
    while col_star<=5-row:
        print("* ",end=" ")
        col_star+=1
    print()
    row-=1
 

#For loop:

#Ex:1

for g in range(1,7):
    for h in range(5):
        print(g,end=" ")
print()

#Ex:2

for g in range(1,7):
    for h in range(1,g):
        print(h,end=" ")
print()

#Ex:3

for g in range(1,7):
    for h in range(1,g):
        print(h,end=" ")
        print("*",end=" ")
    print()

#Ex.4

for g in range(1,7):
    for h in range(1,g):
        print(h,end=" ")
for m in range(1,6):
    print("*",end=" ")
print()