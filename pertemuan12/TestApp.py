from Globals import*            # import library Globals.py
from MyLib import*              #import library Mylib.py

N=0
while True:
    N=int(input("Panjang Array yang ingin diisi:"))
    if N>Nmin and N<Nmax:
        break

global X
global NMin
print("-----input Array-----")
for i in range(Nmin,N):
        X[i]=float(input("indeks ke-"+str(i)+":"))

print("Jumlah =",Jumlah(N))
print("Mean =",Mean(N))
print("Median =",Median(N))
print("Min =",Min(N))
print("Max =",Max(N))


