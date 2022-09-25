def datenverarbeitung(liste,name,persNr,datum):
    import datetime
    listeMitSubListen =[]
    subList =[]
    for x in range(0,20,4):
    
        A_Beginn = liste[x].get()
        A_Ende = liste[x+1].get()
        P_Beginn = liste[x+2].get()
        P_Ende = liste[x+3].get()
        subList = [A_Beginn,P_Beginn,P_Ende,A_Ende] #Jedes Zeitobjekt beinhaltet die Zeiten des Tages
        print("Tag:",subList)
        listeMitSubListen.append(subList)
    print(listeMitSubListen)
    #### Daten in Excel schreiben ####
    import xlsxwriter
    workbook = xlsxwriter.Workbook('Arbeitszeiten.xlsx')
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format()
    cell_format.set_font_color('green')

    list0 = ["P-Nr.","Vorname Nachname","Datum","Zeit","Typ","Bemerkung"]
    worksheet.set_column(0, 0, 14)   # Column  A   width set to 20.
    worksheet.set_column(1, 1, 30)   # Columns B-D width set to 30.
    worksheet.set_column(2, 5, 15)
    ## column beschreibungen
    for i,item in enumerate(list0):
        worksheet.write(2,i,item)
    ## Die grünen Datensätze
    row = 2
    typ = ""
    bemerkung = ""
    for i2,Tag in enumerate(listeMitSubListen):
        if Tag[0] != "" and Tag[3] != "":        ## checkt, ob an dem Tag gearbeitet wurde (gibt es einen Arbeitsbeginn..)

            for i,time in enumerate(Tag):
                row +=1
                if i == 0:
                    typ = "P10"
                    bemerkung = "Kommen"
                elif i == 1:
                    typ = "P15"
                    bemerkung = "Beginn Pause"
                elif i == 2:
                    typ = "P25"
                    bemerkung = "Ende Pause"
                elif i == 3:
                    typ = "P20"
                    bemerkung = "Gehen"
                    
                else:
                    typ = "FEHLER!"
                datum1 = datetime.datetime.strptime(datum, "%Y-%m-%d") 
                datum2 = datum1 + datetime.timedelta(days=i2)
                datum3 = datum2.strftime("%d.%m.%Y")
                print(datum3)
                ########### DATEN ###########
                test = [persNr,name,datum3,time,typ,bemerkung] 
                ########### DATEN ###########
                worksheet.write_row(row,0,test,cell_format)
              
                
    workbook.close()
    return True

    
