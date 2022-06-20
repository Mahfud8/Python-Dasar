# Kamus
bulan = [int]*12
i = 0
# Algoritma
# Inputkan bulan
while i<len(bulan):
    bulan[i]=int(input("bulan ke "+str(i+1)+":"))
    i = i+1
i=0
# Outputkan bulan
while i<len(bulan):
    print("Bulan",bulan[i])
    i = i+1
