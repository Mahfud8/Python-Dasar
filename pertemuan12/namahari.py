# Program NamaHari
# Kamus
arrNamaHari = [str]*7
i = 0
print("inputkan hari:")
# Algoritma
# Inputkan hari
while i<len(arrNamaHari):
    arrNamaHari[i]=input("Hari ke-"+str(i+1)+":")
    i = i+1
#arrNamaHari[0]=1                   #cara akses langsung
#arrNamaHari.append("Hari libur")
i=0
# Outputkan hari
print("Outputkan hari")
while i<len(arrNamaHari):
    print("Hari ke-"+str(i+1)+":",arrNamaHari[i])
    i = i+1
