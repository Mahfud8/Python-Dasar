from Globals import *                     #import dari Globals.py
def CheckOnOff():
    ''' langsung mengembalikan global g_onoff
    '''
    global g_onoff
    return g_onoff
def TurnOnoff():
    ''' Jika CheckOnOff() bernilai true maka global g_onoff diberi
    nilai False, selain itu global g_onoff diberi nilai True
    '''
    global g_onoff
    if CheckOnOff()==True :                 #jika AC hidup
        print("AC mati")
        g_onoff=False                       #AC dimatikan
    else:                                   #jika AC mati
        print("AC hidup")
        g_onoff=True                        #AC dihidupkan
        #Display()
    
def TempUp():
    ''' Menaikkan temperatur suhu hanya 1 derajat per pemanggilan
    prosedur ini. Update nilai global g_temp dengan g_temp+1
    Initial state (syarat prosedur ini bekerja): CheckOnOff()
    bernilai true`
    '''
    global g_temp
    if CheckOnOff()==True :                 #AC dalam kondisi hidup
        if g_temp<28:                       #batas suhu tertinggi 28
            g_temp=g_temp+1
            #Display()
        else:
            print("suhu maksimal")  
    else:
        print("AC mati")
def TempDown():
    ''' Menurunkan temperatur suhu hanya 1 derajat per pemanggilan
    prosedur ini. Update nilai global g_temp dengan g_temp-1
    Initial state (syarat prosedur ini bekerja): CheckOnOff()
    bernilai true
    '''
    global g_temp
    if CheckOnOff()==True :                 #AC dalam kondisi hidup
        if g_temp>18:                       #batas suhu terendah 18
            g_temp=g_temp-1
            #Display()
        else:
            print("suhu minimal")   
    else:
        print("AC mati")    
def FanSpeed():
    ''' Menaikkan nilai level kipas, namun demikian, jika level
    kipas sudah mencapai batas maksimum yaitu 4, maka level
    kipas akan menjadi 1, update nilai global g_fanlevel
    Initial state (syarat prosedur ini bekerja): CheckOnOff()
    bernilai true
    '''
    global g_fanlevel
    if CheckOnOff()==True :                 #AC dalam kondisi hidup
        if g_fanlevel<4:                    #batas maksimum level kipas 4
            g_fanlevel=g_fanlevel+1
        else:
            g_fanlevel=1                    #level kipas kembali ke-1
        #Display()
    else:
        print("AC mati")
def PowerChill():
    ''' Langsung memberikan nilai g_temp dengan nilai terendah dan
    g_fanlevel dengan nilai tertinggi.
    Initial state (syarat prosedur ini bekerja): CheckOnOff()
    bernilai true
    '''
    global g_temp
    global g_fanlevel
    if CheckOnOff()==True :                 #AC dalam kondisi hidup
        g_temp=18                           #suhu terendah
        g_fanlevel=4                        #level kipas maksimum
        #Display()
    else:
        print("AC mati")
def Display():
    ''' Mengoutputkan status suhu dan level kipas saat ini.
    Yang dioutputkan adalah g_temp dan g_fanlevel.
    Initial state (syarat prosedur ini bekerja): CheckOnOff()
    bernilai true
    '''
    global g_temp
    global g_fanlevel
    if CheckOnOff()==True :                 #AC dalam kondisi hidup
        print("Temperature:",g_temp)        #menampillkan temperatur
        print("Fan Speed:",g_fanlevel)      #menampilkan level kipas
    else:
        print("AC mati") 
