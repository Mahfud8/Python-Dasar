#Sengketa Lahan
#kamus
p = float(input("masukan panjang lahan: "))
l = float(input("masukan lebar lahan: "))
k = (input("setuju/tidaksetuju: "))
#Algoritma
if (k=="setuju"):
	print("luas lahan: ",p*l)
	print("luas lahan setelah dibagi: ",(p*l)/2)
if (k=="tidak setuju"):
	print("luas lahan: ",p*l)
	print("luas lahan tidak dibagi: ",p*l)
	