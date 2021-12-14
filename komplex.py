from math import sqrt

class KomplexCislo:
    """Trida komplexnich cisel ve fromatu a + ib"""
    def __init__(self,x,y):
        """Inicializuje komp. cislo ve fromatu a + ib"""
        self.a = x
        self.b = y

    def __str__(self):
        """Vypise komplexni cislo"""
        if self.b < 0:
            return f"{self.a}{self.b}i"
        else:
            return f"{self.a}+{self.b}i"

    def pricti(self, other):
        """K puvodnimu cislu pricte cislo nove"""
        self.a = self.a + other.a
        self.b = self.b + other.b

    def __eq__(self, other):
        """Porovna komplexni cisla, zda jsou stejna"""
        return self.a == other.a and self.b == other.b

    def velikost_cisla(self):
        """Vrati velikost komplexniho cilsa"""
        return sqrt(self.a * self.a + self.b * self.b)

    def vynasob(self,other):
        """Vynasobi puvodni cilso jinym komplexnim cislem"""
        self.a = self.a * other.a - self.b * other.b
        self.b = self.a * other.b + self.b * other.a
        

    

    


        

    

    
