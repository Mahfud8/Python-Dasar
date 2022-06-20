L = list(map(int,input("Masukan Tahun : ").split(" ")))
tahun=[]
jumlah=0
for i in L:
    if i >=1990 and i<=2020:
        if i%2==1:
            jumlah+=1
            tahun.append(i)
    else:
        print("Tahun",i,"tidak valid")

if len (tahun)>0:
    tahun=sorted(tahun)
    print("Tahun kemenangan semarang chester")
    for i in tahun:
        print(i)
print("jumlah kemenangan semarang chester = ",jumlah)        