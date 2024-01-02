import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        return f"Le cercle a un rayon de {self.rayon}, une circonférence de {self.circonference()}, un diamètre de {self.diametre()} et une aire de {self.aire()}."

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Exemple d'utilisation :
cercle1 = Cercle(4)
cercle2 = Cercle(7)

print(cercle1.afficherInfos())  
print(cercle2.afficherInfos())  
