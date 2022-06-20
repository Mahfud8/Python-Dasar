from MyLib import*                              #import MyLib.py
def main(): 
    data = "balonku ada lima, rupa-rupa warnanya" 
    print("data:",data)     
    c1 = input("c1:")                           # inputan untuk variabel c1,c2, dan p 
    c2 = input("c2:") 
    p = input("p:") 
    print(panjangString(data))                  # panjangString dengan parameter aktual data  
    cariKarakter(c1,data)                       # cariKarakter dengan parameter aktual data dan c1 
    print(frekuensiKarakter(c2,data))           # frekuensiKarakter dengan paramter aktual data dan c2 
    if cekPalindrom(p):                         # jika cekPalindrom(P) bernilai True outputkan “palindrom” 
        print("palindrom") 
    else:                                       # jika tidak outputkan “bukan palindrom” 
        print("bukan palindrom") 
if __name__ == "__main__": 
    main() 
