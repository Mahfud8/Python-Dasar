#kamus
t=int(input("jumlah testcase:"))
i=1
#algoritma
while (i<=t):
    i=i+1
    a=int(input("masukkan angka :"))
    if a>=0 and a<=9:
        if a==0 or a==6 or a==9:
            print("jumlah korek yang dibutuhkan 6")
        elif a==1:
            print("jumlah korek yang dibutuhkan 2")
        elif a==2 or a==3 or a==5:
            print("jumlah korek yang dibutuhkan 5")
        elif a==4:
            print("jumlah korek yang dibutuhkan 4")
        elif a==7:
            print("jumlah korek yang dibutuhkan 3") 
        elif a==8:
            print("jumlah korek yang dibutuhkan 7")
    else:
         print(invalid)
    
