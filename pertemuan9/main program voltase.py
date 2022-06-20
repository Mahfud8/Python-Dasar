import voltase		

def main():
    #kamus
    R = int(input())
    A = int(input())	
    #algoritma
    voltase.HitungVoltase(R,A)
    v = voltase.HitungVoltase2(R,A)
    print(v)

if __name__ == '__main__':
    main()
