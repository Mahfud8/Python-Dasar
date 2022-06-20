#kamus
saldoawal= int(input("masukan saldo: "))
sisasaldo=saldoawal
pengeluaran=0
#algoritma
while (pengeluaran!=-1):
    pengeluaran=int(input("pengeluaran soni hari ini: "))
    if((pengeluaran>0) and (sisasaldo-pengeluaran)):
        sisasaldo=sisasaldo-pengeluaran
    else:
        if (pengeluaran!=-1):
            printt("sisa saldo tidak cukup",end="")
        break
print ("sisa saldo = ",sisasaldo)
