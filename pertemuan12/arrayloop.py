# for loop
a=[int]*4
# input
for i in range (len(a)):
    a[i]=int(input(a))
a.append(5)
# output
for i in range(len(a)):
    print(a[i])  


# while loop
b=[int]*4
i=0
# input
while i<len(b):
    b[i]=input(b)
    i+=1
# output
i=0
while i<len(b):
    print(b[i])
    i+=1        