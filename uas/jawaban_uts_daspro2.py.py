#{kasus2}
#kamus
namaPegawai = input("Masukan nama pegawai : ")
golongan = input("Masukab gol : ")
jabatan = input("Masukan jabatan : ")
#algortima
if golongan == "gol-1" :
    gajipokok = 3000000
    print("Gaji pokok : ",gajipokok)
elif golongan == "gol-2" :
    gajipokok = 5000000
    print("Gaji pokok : ",gajipokok)
else :
    gajipokok = 7000000
    print("Gaji pokok : ",gajipokok)
if jabatan == "staff" :
    tunjangan = 0
    print("tunjangan : ",tunjangan)
elif jabatan == "supervisor" :
    tunjangan = 1000000
    print("tunjangan : ",tunjangan)
else :
    tunjangan = 2000000
    print("tunjangan : ",tunjangan)
gajikotor = gajipokok + tunjangan
print("gaji kotor : ",gajikotor)
if gajikotor > 5000000 :
    pajak = 5/100
    print("Pajak : ",pajak)
else :
    pajak = 0
    print("pajak : ",pajak)
if pajak == 5/100 :
    gajibersih = gajikotor - gajikotor*pajak
    print("gaji bersih : ",gajibersih)
else :
    gajibersih = gajikotor
    print("gaji bersih : ",gajibersih)
