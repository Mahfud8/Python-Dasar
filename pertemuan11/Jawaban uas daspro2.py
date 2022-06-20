L=[]

def sum():
    global L
    s=0
    if L is not None:
        for i in L:
            if i%2==1:
                s+=i
    return s

def maks():
    global L
    max=L[0]
    if len(L)>0:
        for i in L:
            if i>max and i%2==1:
                i=max
                
    return i
   
def main():
    i=1
    global L
    L = list(map(int,input().split(" "))) 
    

    print("jumlah genap:",sum())
    print("maks genap:",maks())  

if __name__=="__main__":
    main()