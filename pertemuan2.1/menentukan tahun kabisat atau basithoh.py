#menentukan tahun kabisat atau bashithoh
tahun=int(input("Masukan tahun : "))

if (tahun % 400) == 0:
    print (tahun, "merupakan tahun kabisat")
elif (tahun % 100) == 0:
    print (tahun,"merupakan tahun basithoh")
elif (tahun % 4) == 0:
    print (tahun, "merupakan tahun kabisat")
else:
    print (tahun,"merupakan tahun basithoh")
   