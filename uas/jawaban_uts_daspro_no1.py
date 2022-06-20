#program menghitung jumlah deret n bilangan
#kamus
nama=(input("Nama MHS:"))
namamatakuliah=(input("Nama Matakuliah:"))
nilaitugas=int(input("Nilai Tugas:"))
nilaiuts=int(input("Nilai UTS:"))                 
nilaiuas=int(input("Nilai UAS:"))
#algoritma
print("------------------")
print("Transkripsi Nilai")
print("------------------")
print("Nama MHS:",nama)
print("Nama matakuliah:",namamatakuliah)
nilaiakhir= (40/100*nilaiuas)+(30/100*nilaiuts)+(30/100*nilaitugas)
print("Nilai Akhir:",(nilaiakhir))
if(nilaiakhir>0)and (nilaiakhir<=100):
    if (nilaiakhir<=39):
        print("keteragan:E")
    elif(39<nilaiakhir<=50):
        print("Keterangan:D")
    elif (50<nilaiakhir<=55):
        print("Keterangan:C-")
    elif (55<nilaiakhir<=60):
        print("Keterangan:C+")
    elif (60<nilaiakhir<=65):
        print("Keterangan:B-")
    elif (65<nilaiakhir<=69):
        print("Keterangan:B+")
    elif (69<nilaiakhir<=74):
        print("Keterangan:B")
    elif (74<nilaiakhir<=79):
        print("Keterangan:B+")
    elif (79<nilaiakhir<=84):
        print("Keterangan:A-")
    elif (nilaiakhir>=84):
        print("Keterangan:A")
else:
    print("nilai tidak valid")