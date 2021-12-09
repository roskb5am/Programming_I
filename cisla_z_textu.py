#vypsání jen čísel z textu, cisla na radku v puvidnim souboru maji byt na stejnem radku i v novem souboru 
soubor_in = open("soubor.txt","r")          #otevreni souboru pro cteni
soubor_out = open("soubor_s_cisly.txt","w") #otevreni souboru pro zapis

for line in soubor_in:                      
    for i in range(len(line)):              #pro kazdy radek
        if line[i] == "\n":                 #kdyz znak noveho radku
            soubor_out.write("\n")          #zapisu ho do noveho souboru, mam drzet radkovou strukturu
            
        if line[i].isdigit():               #pokud narazim na cislo
            if line[i+1].isdigit():         #pokud je i dalsi znak cislo
                soubor_out.write(line[i])   #zapisu jen to cislo
            else:
                soubor_out.write(line[i]+" ")   #jinak zapisu cislo a mezeru, pac je to konec toho cisla

soubor_in.close()
soubor_out.close()

