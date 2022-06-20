L=[]

def sum():
    global L
    s=0
    if L is not None:
        for i in L:
            s+=i
    return s
    #return sum(L)

def mean():
    global L
    l=0
    if L is not None:
        for i in L:
            l+=1
    return sum()/l
    #return sum()/len(L)  

def median():
    global L
    l=sorted(L)
    #print("sorted L-",l)
    if l is not None: 
        if len(l)%2==1:
            return l[int((len(l)/2))]
        else:
            return(l[int((len(1)/2))]+[int((len(1)/2))-1])/2

def min():
    global L
    min=L[0]
    if len(L)>0:
        for i in L:
            if i<min:
                min=i
    return min 
    #return min(L)

def maks():
    global L
    max=L[0]
    if len(L)>0:
        for i in L:
            if i>max:
                max=i
    return max
    #return max(L)

def main():
    i=1
    global L
    #L = list(map(int,input().split(" ")))
    while True:
        el=float(input("masukan list ke-"+str(i)+": "))
        if el==0:
            break
        else:
            L.append(el)
        i+=1

    print("L",L)
    print("sum L:",sum())   
    print("mean L:",mean())
    print("median L:",median())
    print("min L:",min())
    print("maks L:",maks())

if __name__=="__main__":
    main()