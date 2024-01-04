class Student:
    def __init__(self, nom, prenom, numero, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = credits
        self.__level = self.__studentEval()
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__numero}")
        print(f"Niveau = {self.__level}")

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Error: Credits est a  zero.")

    def print_credits(self):
        print(f"Le nombre de credits de {self.__nom} {self.__prenom} est de {self.__credits} points")


student = Student("John", "Doe", 145)


student.add_credits(10)
student.add_credits(10)
student.add_credits(10)

student.print_credits()

    
    