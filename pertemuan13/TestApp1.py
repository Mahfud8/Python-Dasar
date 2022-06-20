from MyLib1 import *      #import library Mylib1.py jika beda file

def main():
 # input
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    jmlmakul = int(input("masukan Jumlah Mata Kuliah : "))
    m=input("masukan mata kuliah : ")
    a=int(input("masukan nilai : "))
   
    print(inputNilai())
    #print(inputMakul())
    print(DisplayTranskrip())

#panggil main program disini
main()