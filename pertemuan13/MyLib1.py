nilai=[]
makul=[]
nA=[]
nH=[]
nilai=[makul,nA,nH]

def inputNilai(nama,angka,huruf):
    global makul
    global nA
    global nH

    makul.append(nama)
    nA.append(angka)
    nH.append(huruf)

    n=0
    ipk=0
    while n<jmlmakul:
        if a>85 and a<=100:
            inputNilai(m,a,'A')
            ipk+=4
            n+=1
        elif a>=70:
            inputNilai(m,a,'B')
            ipk+=3
            n+=1
        elif a>=60:
            inputNilai(m,a,'C')
            ipk+=2
            n+=1
        elif a>=50:
            inputNilai(m,a,'D')
            ipk+=1
            n+=1
        elif a>=0:
            inputNilai(m,a,'E')
            n+=1
        else:
            print("nilai salah")
    
def DisplayTranskrip():
    print("NIM : ",nim)
    print("Nama : ",nama)

    global nilai
    for i in range(jmlmakul):
        print("Makul",nilai[0][i],"Nilai Angka",nilai[1][i],"Nilai Huruf",nilai[2][i])

    #hitung ipk
    ipk=ipk/jmlmakul
    print("IPK : ",ipk)
    if ipk>=3.5:
        print("Cumlaude")
    else:
        print("Tidak Cumlaude")

