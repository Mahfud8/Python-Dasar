# Kamus
a = 1
b = 4
# Algoritma
print("Hasil a yang pertama:", a)
print("Hasil b yang pertama:"+str(b))
b = a + 1 
a -= b #ini ekuivalen dengan a = a - b
print("Hasil a yang kedua : "+str(a))
print("Hasil b yang kedua:",b)
a = b + 2
b = a * b
print("Hasil a yang ketiga: {}".format(a))
print("hasil b yang ketiga: %f" % (b))
c = a
a = a * 2
b = c
print("Hasil a yang keempat: {}".format(a))
print("Hasil b yang keempat: {}".format(b))