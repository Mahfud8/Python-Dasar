fungsi kecepatan (s,t) -> integer
{fungsi menghitung kecepatan}
kamus
v=integer
algoritma
v=s/t
-> v

------------------------------------
program mengunakan fungsi kecepatan
kamus
input (s)
input (t)
v=kecepatan(nilai)
output (v)

------------------------------------
def kecepatan (s,t):
    #fungsi menghitung kecepatan
    #kamus
    v=0
    #algoritma
    v=s/t
    return v

#program mengunakan fungsi kecepatan
#kamus
s=0
t=0
#algoritma
s=int(input("s="))
t=int(input("t="))
x=kecepatan(nilai)
print("kecepatan =",x)
