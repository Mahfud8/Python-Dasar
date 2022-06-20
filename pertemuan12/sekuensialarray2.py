NMin = 1
NMax = 10
T = [int]*NMax
x = 0                                    # atau x=NMin-1
i = 0                                    #indeks mulai dari 0
x = int(input("Masukan Angka:"))
while x != 9999 and i<NMax:              #jika x=9999 dan i<NMax  loop berhenti
    T[i] = x
    i = i + 1
    if x==9999 or i>=NMax:
        break
    x = int(input("Masukan Angka:"))
if i>NMax:
    print("array penuh")
if i>0:
    for j in range(NMin-1,i):
        print("Array ke-",j,":",T[j])
else:
    print("array masih kosong")
    