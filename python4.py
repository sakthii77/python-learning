
#List Functions

#Len()

a=[1,2,3,4]
b=[10,20,30,40]
c=[60,70,80,90]
d=[5,6,7,8]
e=[a,b,c,d]
f=[a+b+c+d]
g=a+b+c+d
h=a,b,c,d
print(a)
print(len(a))
print(e)
print(len(e))
print(f)
print(len(f))
print(g)
print(len(g))
print(h)
print(len(h))

#Count()

a=[1,2,3,4,2,2,2,2]
print(a.count(2))

#How the count function internally works?:

a=[1,2,3,4,2,2,2,2]
b=2
i=0
count=0
while i<len(a):
    if a[i]==b:
        count+=1
    i+=1
else:
    print(count)

#Append()

a=[1,2,3,4,2,2,2,2]
print(id(a))
a.append(132)
b=a
print(id(b))
print(b)

#Ex:1

a=[]
i=0
for new in range (0,50):
    a.append(new)
print(a)

#insert()

a=[10,20,30,40,50,]
a.insert(3,455)
print(a)

#ex:2

a=[10,20,30,40,50]
a.insert(3,455)
print(a)
a.insert(-5,255)
print(a)
a.insert(-300,255)
print(a)

#Extent()

a=[10,20,30,40,50]
b=[1000,2000]
print(a+b)
a.extend(b)
print(a)

#Remove:

a=[10,20,30,40,50]
b=[1000,2000]
a.remove(20)
print(a)

#pop()

a=[10,20,30,40,50]
b=[1000,2000]
a.pop()
print(a)
b.pop()
print(b)

#Reverse()

a=[10,20,30,40,50]
b=[1000,2000]
a.reverse()
print(a)
b.reverse()
print(b)

#bubble sort()

a=[50,40,30,20,10]
b=[2000,1000]
a.sort()
print(a)
b.sort()
print(b)


