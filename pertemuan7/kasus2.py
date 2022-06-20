#Kamus
n = int(input())
#Algoritma
for i in range(n):
     t = int(input())            #jumlah baris segitiga
     for num in range(t+1):      #membuat baris
         for j in range(num):    #membuat kolom
            print (num, end=" ") #print number
         # supaya membuat baris baru pada segitiga
         print("\n")             #enter 

