i = 0
NMin = 0
NMax = 100
T = [int]*NMax
N = 0
print(T)
#menentukan jumlah indeks yang  ingin diinput
while True:
    N = int(input("panjang Array yang ingin diisi:"))
    if N > NMin and N <= NMax:              # N > NMin karena indeks minimal 1
        break

#input array T
print("---------Input Array---------")    
for i in range(NMin,N):
    T[i] = int(input("indeks ke-"+str(i)+":"))
#output array T
print("-------Cetak isi Array-------")
for i in range(NMin,N):
    print("indeks ke-"+str(i)+":",T[i])
