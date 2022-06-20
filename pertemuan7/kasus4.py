
#kamus
IPK = 0
counter = 0
n = int(input("Masukkan batas makul: "))
#Algoritma

while counter<n:
 nilai = int(input("nilai makul ke-"+str(counter+1)+":"))
 if nilai >= 85:
     IPK += 4 #sama dengan IPK=IPK+4
 elif nilai >=70 and nilai <85:
     IPK += 3
 elif nilai >=60 and nilai <70:
     IPK += 2
 elif nilai >=50 and nilai <60:
     IPK += 1
 counter += 1
print("IPK:", IPK/counter)

