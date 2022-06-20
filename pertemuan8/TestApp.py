from MyLib import *   #import library Mylib.py berlaku jika subprogram di file terpisah
def main():
 # input
 angka1 = int(input("Masukkan angka pertama untuk aritmatika:"))
 angka2 = int(input("Masukkan angka kedua untuk aritmatika:"))
 s = float(input("Masukkan sisi persegi (float):"))
 a,t = map(float,input("Masukkan a & t segitiga (float)(float):").split())

 #output dengan memanggil fungsi pada aritmatika untuk masukan int
 print("Hasil Penjumlahan:", Tambah(angka1,angka2))
 print("Hasil Pengurangan:", Kurang(angka1,angka2))
 #berikut ini contoh men-assign hasil fungsi ke variable
 hasilkali = Kali(angka1,angka2)
 print("Hasil Perkalian:", hasilkali)
 print("Hasil Pembagian:", Bagi(angka1,angka2))
 print("Luas Persegi:", LuasPersegi(s))
 print("Luas Segitiga:", LuasSegitiga(a,t))
#panggil main program disini

main()