class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom du produit : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}, Prix TTC : {self.CalculerPrixTTC()}"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def retournerNom(self):
        return self.nom

    def retournerPrixHT(self):
        return self.prixHT

    def retournerTVA(self):
        return self.TVA


produit1 = Produit("Produit 1", 100, 20)
produit2 = Produit("Produit 2", 200, 15)

print(produit1.afficher())  
print(produit2.afficher())  

produit1.modifierNom("Nouveau Produit 1")
produit1.modifierPrix(150)

produit2.modifierNom("Nouveau Produit 2")
produit2.modifierPrix(250)

print(produit1.afficher())  
print(produit2.afficher())  
