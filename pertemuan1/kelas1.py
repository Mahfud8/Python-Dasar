#import math
#program menghitung jarak 2 pesawat
#kamus
rdr_kpl=9
rdr_pswt1=10
rdr_pswt2=12
#algoritma
rdr_kpl=int(input("jarak radar ke kapal induk = "))
rdr_pswt1=int(input("jarak radar dengan pesawat 1= "))
rdr_pswt2=int(input("jarak radar dengan pesawat 2= "))

kpl_pswt1 = math.sgrt(math.pow(rdr_pswt1,2)-math.pow(rdr_kpl,2))
kpl_pswt2 = math.sgrt(math.poww(rdr_pswt2,2)-math.pow(rdr_kpl,2))
jarak = kpl_pswt2-kpl_pswt1

print ("jarak antara pesawat 1 dan pesawat 2 =", jarak)
