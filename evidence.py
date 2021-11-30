evidence = [{"jmeno": "Straka", "evidencni cislo": 101, "barva": ["hneda","bila"],"dojivost": 25},
            {"jmeno": "Milka", "evidencni cislo": 203, "barva": ["fialova","bila"], "dojivost": 40},
            {"jmeno": "Cervenka", "evidencni cislo": 152, "barva": ["cervena"], "dojivost": 35}]

def index_kravy(hledana_krava,vypis=0):
    for i in range(len(evidence)):
        krava = evidence[i]
        if krava["jmeno"] == hledana_krava:
            return i 
    else:
        if vypis:
            print("Krava", hledana_krava, "neni v evidenci")
        return None
        
def info_kravy(hledana_krava):
    index = index_kravy(hledana_krava,0)
    if index != None:
        for a, b in evidence[index].items():
            print(f"{a}: {b}")
        print()
    else:
        print("Krava", hledana_krava, "neni v evidenci")

def pridej_kravu(jmeno, cislo, barvy, dojivost):
    index = index_kravy(jmeno)
    if index == None:
        nova_krava = {"jmeno": jmeno, "evidencni cislo": cislo, "barva": barvy, "dojivost":dojivost}
        evidence.append(nova_krava)
    else:
        print("Krava je jiz v evidenci")

def odstran_kravu(jmeno):
    index = index_kravy(jmeno)
    if index != None:
        del evidence[index]
    else:
        print("Krava jiz v evidenci neni")

info_kravy("Straka")

pridej_kravu("Rohata",432,["bezova"],33)

info_kravy("Rohata")

odstran_kravu("Milka")
