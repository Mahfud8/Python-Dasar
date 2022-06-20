from Globals import*
def Jumlah(N):
    global X
    global Nmin
    s=0
    for i in range(Nmin,N):
        s+=X[i]
    return s

def Mean(N):
     return Jumlah(N)/N

def Median(N):
    global X
    global Nmin
    t=[float]*N
    for i in range(Nmin,N):
        t[i]=X[i]
    t=sorted(t)
    print("Sorted X=",t)
    if len (t)%2==1:
        return t[int(N/2)]
    else:
        return(t[int(N/2)]+t[int(N/2)-1])/2

def Min(N):
    global X
    min=X[0]
    for i in range (Nmin+1,N):
        if X[i]<min:
            min=X[i]
    return min

def Max(N):
    global X
    max=X[0]
    for i in range (Nmin+1,N):
        if X[i]>max:
            max=X[i]
    return max