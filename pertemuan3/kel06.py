#c = sisi miring
#b = sisi alas
#a = tinggi dalam**2

print("PROGRAM MENGHITUNG JARAK 2 PESAWAT BERDASARKAN TINGGINYA")
print("\n====TINGGI PESAWAT A====\n")
c = float (input ("Sisi miring :"))
b = float (input ("Sisi alas :"))
a = c**2 - b**2
tinggi_pesawatA = (a**0.50)
print("Tinggi pesawat A adalah =",tinggi_pesawatA)

print("\n====TINGGI PESAWAT B====\n")
c = float (input ("Sisi miring :"))
b = float (input ("Sisi alas :"))
a = c**2 - b**2
tinggi_pesawatB = a**0.50
print("Tinggi pesawat B adalah =",tinggi_pesawatB)

jarak_kedua_pesawat = tinggi_pesawatB - tinggi_pesawatA
print("Jadi jarak kedua pesawat adalah :",jarak_kedua_pesawat) 
