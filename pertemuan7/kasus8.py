#kamus
import random
N=int(input("Masukan saldo awal: "))
t=int(input("Kapan tanggal lahir Mama: "))
s=0
#algoritma
if t==12:
    M=int(input("Masukkan jumlah pulsa yang diinginkan Mama:"))
    if N>=M:
        for i in range (3):
            r=random.random()
            print ("mohon tunggu.....")
            if (r>0.5):
                print ("transaksi berhasil")
                s=1
                break
        if s==0:
            print ("transaksi gagal")
    else:
        print ("saldo tidak cukup")
else:
        print("ini penipu")
