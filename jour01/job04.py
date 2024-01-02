class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Example usage:
person1 = Personne("Doe", "John")
person2 = Personne("Dupond", "Jean")

print(person1.SePresenter())  # Output: Je suis John Doe
print(person2.SePresenter())  # Output: Je suis Jean Dupond


