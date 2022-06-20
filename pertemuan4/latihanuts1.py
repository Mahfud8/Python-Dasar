#kamus
tahun=int(input("masukan tahun: "))
#algoritma
if (tahun > 0) and (tahun %4 == 0):
    if( tahun%100 !=0) or (tahun%400==0):
        print("Tahun", tahun)
        print("merupakan tahun kabisat")
    else:
        print("Tahun", tahun)
        print("bukan tahun kabisat")
else:
    print("tahun tidak valid")