def fx1 (x):
    #fungsi menghitung persamaan x)
    #kamus
    hasil=0
    #algoritma
    hasil=2*(x*x)+(2*x)+1
    return hasil

#program mengunakan fingsi fx1
#kamus
nilai=0
#algoritma
nilai=int(input("x="))
y=fx1(nilai)
print("y=",y)
