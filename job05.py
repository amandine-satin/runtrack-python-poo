class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"Les coordonnées du point sont ({self.x}, {self.y})"

    def afficherX(self):
        return self.x

    def afficherY(self):
        return self.y

    def changerX(self, newX):
        self.x = newX

    def changerY(self, newY):
        self.y = newY


point1 = Point(2, 3)
print(point1.afficherLesPoints()) 
print(point1.afficherX())  
print(point1.afficherY())  
point1.changerX(5)
point1.changerY(6)
print(point1.afficherLesPoints())  
