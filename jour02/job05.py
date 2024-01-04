class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Le réservoir est vide. La voiture ne peut pas démarrer.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir > 5

    def studentInfo(self):
        print(f"Marque = {self.__marque}")
        print(f"Modèle = {self.__modele}")
        print(f"Année = {self.__annee}")
        print(f"Kilométrage = {self.__kilometrage}")
        print(f"En marche = {self.__en_marche}")
demarrer = Voiture()
demarrer.studentInfo()
print(demarrer.studentInfo())