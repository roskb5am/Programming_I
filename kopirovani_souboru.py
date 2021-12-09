#kopírování souboru tak jak je
soubor_in = open("soubor.txt","r")          #otevreni souboru pro cteni
soubor_out = open("soubor_stejny.txt","w")  #otevreni souboru pro zapis

for line in soubor_in:                      #nacte radek puvodniho souboru
    soubor_out.write(line)                  #zapise ji do noveho

soubor_in.close()
soubor_out.close()

#kopírování souboru s opačným pořadím řádků
soubor_in = open("soubor.txt","r")                  #otevreni souboru pro cteni
soubor_out = open("soubor_opacne_radky.txt","w")    #otevreni souboru pro zapis

radky = []                                          #vytvořím seznam řádků

for line in soubor_in:                      
    radky.append(line)

#pozor, radky obsahuji i znak novy radek "\n"
#musim tedy osetrit:
#prvni radek, ktery se stane poslednim, aby tam nemel znal "\n"
radky[0] = radky[0][:-1]                            #udelam rez, kde se zbavim posledniho znaku
#posledni radek, ktery se stane prvnim, aby tam mel "\n"
radky[-1] += "\n"                                   #upridam konec radku

for i in range(len(radky),0,-1):
    soubor_out.write(str(radky[i-1]))

#alternativne vytvorim seznam radku v opacnem poradi
#radky_opacne = radky[::-1]
#a pak je zapisu
#for dilci_radek in radky_opacne:
#    soubor_out.write(dilci_radek)

soubor_in.close()
soubor_out.close()

#kopírování souboru s opačným pořadím řádků i slov
soubor_in = open("soubor.txt","r")                  #otevreni souboru pro cteni
soubor_out = open("soubor_opacne_radky_i_slovy.txt","w")    #otevreni souboru pro zapis

radky = []                                          #vytvořím seznam řádků

for line in soubor_in:                      
    radky.append(" ".join(line.rstrip().split()[::-1])) #radek zbavim znaku konce radku
                                                        #rozdelim na slova a zmenim jejich poradi
                                                        #opet vse spojim s mezerami jako delitkem
radky_opacne = radky[::-1]

for i in range(len(radky_opacne)):
    soubor_out.write(radky_opacne[i])
    if(i != len(radky_opacne)-1):
           soubor_out.write("\n")                       #prida novy radek krome toho posledniho

soubor_in.close()
soubor_out.close()
