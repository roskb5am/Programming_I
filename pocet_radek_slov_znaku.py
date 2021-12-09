#počet řádků
with open("soubor.txt","r") as soubor_in:   #pouzit context manageru
    pocet_radku = 0
    for line in soubor_in:
        pocet_radku += 1
print("Počet řádků je",pocet_radku)

#počet slov a znaků
soubor_in = open("soubor.txt","r")          #standardni otevreni souboru
pocet_slov = 0
pocet_znaku = 0

for line in soubor_in:
    slova = line.split()
    pocet_slov += len(slova)
    for dilci_slovo in slova:
        pocet_znaku +=len(dilci_slovo)
        
print(f"Počet slov je {pocet_slov}, počet znaků je {pocet_znaku}")
soubor_in.close()                           #soubor nesmim zapomenout zavrit



