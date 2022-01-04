class Zvire:
    """trida zvire"""
    def __init__(self, nazev, jmeno, zvuk):
        """inicializuje nazev, jmeno a zvuk"""
        self.nazev = nazev
        self.jmeno = jmeno
        self.zvuk = zvuk
    
    def udelej_zvuk(self):
        """vypise zvuk"""
        print(self.zvuk)
         
    def jak_se_jmenuje(self):
         """vrati jmeno"""
         return self.jmeno

class Pes(Zvire):
    """trida pes"""
    def __init__(self, jmeno, zvuk, povel):
        """inicializuje nazev, jmeno, zvuk a povel"""
        Zvire.__init__(self,"pes", jmeno, zvuk)
        self.povel = povel

    def prikaz_povel(self):
        """prikaze povel"""
        print(self.povel,"!!!")

psisko = Pes("Azor","Haf","Aport")
print("Je to",psisko.nazev)                                 #pes ma vsechny atributy zvirete
print("Jmenuje se",psisko.jmeno)
print("Dela",psisko.zvuk)
print("Umi",psisko.povel)                                   #a k tomu navic povel

psisko.prikaz_povel()                                       #prikaz povel je funkce pouze tridy Pes

obecne_zvire = Zvire("zvire","Tvor","")
obecne_zvire.prikaz_povel()                                 #vyusti v chybu, dedicnost jednostranna
