#uang anak kos
#kamus
uangsoni=int(input("masukan uang soni: "))
pengeluaran=1200000
#algoritma
if (uangsoni>pengeluaran):
    if (uangsoni-pengeluaran>=1000000):
        print("soni jadi nonton konser dengan tempat duduk VIP")
    elif (uangsoni-pengeluaran>=500000):
        print("soni jadi nonton konser dengan tempat duduk biasa")
    else:
        print("soni tidak jadi menonton konser karena uang kurang")
        
else:
    print ("uang saku tidak valid")