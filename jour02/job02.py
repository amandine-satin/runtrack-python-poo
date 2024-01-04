class livre:
    def __init__(self, titre, auteur, nombresdepages=100) :
        self.__titre = titre
        self.__auteur= auteur
        self.__nombresdepages = nombresdepages
 
    def get_titre(self) :
     return self.__titre

    def get_auteur(self):
     return self.__auteur

    def get_nombresdepages(self):
     return self.__nombresdepages

    def set_titre(self, titre):
     self.__titre = titre

    def set_auteur(self,auteur):
      self.__auteur = auteur

    def set_nombresdepages(self,nombresdepages):
           if nombresdepages < 0:
            self.__nombresdepages = nombresdepages
           
           else: 
            print("Erreur: Le nombre de pages doit être un entier positif.")
            
Livre = livre("titre", "auteur", 100)
print(f"titre: {Livre.get_titre()}, auteur: {Livre.get_auteur()}, Nombre de pages: {Livre.get_nombresdepages()}")


