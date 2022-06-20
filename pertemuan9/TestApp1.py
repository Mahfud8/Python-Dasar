from MyLib import*                  #import library Mylib.py jika beda file
from Globals import*                #import Globals.py jika beda file
def main():
    while True:
        print("1.On/Off AC")
        print("2.Temp Up")
        print("3.Temp Down")
        print("4.Temp FanSpeed")
        print("5.Power chill")
        i=int(input("masukan: "))
        if i==1:
            TurnOnoff()
            if CheckOnOff()==False :
                break 
        elif i==2:
            TempUp()
        elif i==3:
            TempDown()
        elif i==4:
            FanSpeed()
        elif i==5:
            PowerChill()
        else:
            print("opsi salah")        
        
    
main()