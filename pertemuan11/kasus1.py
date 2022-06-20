#Globals
L=[]
#MyLib
def element list():
    global L
    i=1
    while True:
        el=int(input("masukan eleman list ke-"+str((i))+": "))
        if el==0:
            break
        else:
            L.append(el)
        i+=1
#TestApp
#import globals dan MyLib
global L
print(L)