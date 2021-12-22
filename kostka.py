#variace na hazeni sestistennou kostkou

import random
import statistics

def jednotlive_hody(pocet_hodu):    #vypise zadany pocet jednotlivych hodu
    for _ in range(pocet_hodu):
        print(random.choice([1, 2, 3, 4, 5, 6]))

def hody(pocet_hodu):               #vrati seznam vysledku zadaneho poctu hodu
    return random.choices([1, 2, 3, 4, 5, 6], k=pocet_hodu)
    
print("Par hodu:")           #ukazka hodu
jednotlive_hody(10) 

stredni_hodnota = statistics.mean(hody(10000))  #spocte stredni hodnotu 10k hodu
print("Stredni hodnota 10k hodu je",stredni_hodnota)     #ocekavam 3.5
