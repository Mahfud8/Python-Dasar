#program membaca bilangan bulat yang mewakili suhu air
#kamus
T = 0
#algoritma
T = float(input("masukan suhu :  "))
if (T<0):
	print ("beku")
elif (T>0 and T<100):
	print ("cair")
else
    print ("uap")