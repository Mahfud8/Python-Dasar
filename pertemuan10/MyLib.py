def panjangString(s): 
    counter=0
    for c in s:                     # melakukan pengulangan string (for char in string: )
        counter=counter+1           # teknik penjumlahan 
    return counter


def cariKarakter(c,s): 
    ketemu=False                    # variabel boolean untuk menampung jika karakter ketemu 
    for i in s:                     # melakukan pengulangan string (for char in string: )
        if c==i:
            print("ada")
            ketemu=True             # jika variabel penampung sebelumnya bernilai True maka output “ada” 
            break

    if ketemu==False:               # jika masih False maka outputkan “tidak ada” 
        print("tidak ada")


def frekuensiKarakter(c,s): 
    counter=0 
    for i in s:                     # melakukan pengulangan string (for char in string: )
        if c==i:
            counter=counter+1       # teknik penjumlahan 

    return counter                  # kembalikan 

def cekPalindrom(s): 
    return s==s [::-1]              # cara membalikanya dengan string slicing s[start:stop:step] 