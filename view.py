from model import datenverarbeitung
import tkinter as tk
import datetime
from datetime import date
import os.path




window = tk.Tk()
window.title("Arbeitszeiten in Excel exportieren")
window.geometry("770x320+300+300")
window.resizable(False,False)



window.columnconfigure([0,1,2,3,4,5,6],weight=1,minsize=50)
window.rowconfigure([3,4,5,6,7],pad=7)

label_00 = tk.Label(text="Vor/Nachname")

label_01 = tk.Label(text="PersonalNr.")

label_02 = tk.Label(text="KW Nr.")
label_02.grid(column=0,row=2,sticky="w")
label_010 = tk.Label(text="Made by Philipp Baars")
label_010.grid(column=0,row=10,sticky="w",pady=30,padx=3)

#Wochentage Y-Achse
label_23 = tk.Label(text="Montag")
label_23.grid(column=2,row=3)
label_24 = tk.Label(text="Dienstag")
label_24.grid(column=2,row=4)
label_25 = tk.Label(text="Mittwoch")
label_25.grid(column=2,row=5)
label_26 = tk.Label(text="Donnerstag")
label_26.grid(column=2,row=6)
label_27 = tk.Label(text="Freitag")
label_27.grid(column=2,row=7)

#Spaltennamen X-Achse
label_32 = tk.Label(text="Arbeitsbeginn")
label_32.grid(column=3,row=2)
label_42 = tk.Label(text="Arbeitsende")
label_42.grid(column=4,row=2)
label_52 = tk.Label(text="Pausenbeginn")
label_52.grid(column=5,row=2)
label_62 = tk.Label(text="Pausenende")
label_62.grid(column=6,row=2)

#Entrys
entry_10 = tk.Entry()   #name
entry_11 = tk.Entry()   #pers. nr.
entry_12 = tk.Entry(width=5)    #KW Nr.
#entry_10.grid(column=1,row=0,sticky="w") #für mich angepasste version braucht diese Inputs nicht.
#entry_11.grid(column=1,row=1,sticky="w")
entry_12.grid(column=1,row=2,sticky="w")
eingaben = []
FileExists = bool()

if os.path.isfile('Vorname Nachname - Personalnummer.txt') == False: ### Wenn noch keine Daten erhoben wurden, werden diese Entry Felder angezeigt.
    entry_10.grid(column=1,row=0,sticky="w")
    entry_11.grid(column=1,row=1,sticky="w")
    label_00.grid(column=0,row=0,sticky="w")
    label_01.grid(column=0,row=1,sticky="w")
    FileExists = False
else:
    FileExists = True






for i in range(3,8): # Mon - Fr

    for i2 in range(3,7): # 4 entry fields für jeden tag
        eingabe = tk.Entry()
        eingabe.grid(column=i2,row=i)
        if i2 == 3:
            eingabe.insert(0,"08:00")
        elif i2 == 4:
            eingabe.insert(0,"16:30")
        elif i2 == 5:
            eingabe.insert(0,"11:45")
        elif i2 == 6:
            eingabe.insert(0,"12:45")
        eingaben.append(eingabe)       

def ausgabe():
    if FileExists == False:
        name = entry_10.get()
        persNr = entry_11.get()
        if name == '' or persNr == '':
            window.destroy() #### Programm beendet ####
        else:
            with open('Vorname Nachname - Personalnummer.txt', 'w') as f:
                f.writelines([name,'\n',persNr])

    else:
        with open('Vorname Nachname - Personalnummer.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            name = lines[0]
            persNr = lines[1]
    KwNr = entry_12.get()
    #Datum
    year = date.today().year
    datumString = f"{year}-W{KwNr}"
    datum = datetime.datetime.strptime(datumString + '-1', "%Y-W%W-%w")
    datum = datum.strftime("%Y-%m-%d")
    
    #print(datum)
    checker = datenverarbeitung(eingaben,name,persNr,datum)
    if checker == True:
        window.destroy() #### Programm beendet ####



startButton = tk.Button(text="Start",command=ausgabe)
startButton.grid(column=6,row=9,pady=15)




window.mainloop()
