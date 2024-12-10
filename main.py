import random

class Matrice:
    def __init__(self, size):
        self.size = size 
        self.data = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]


    def __str__(self):#permet d'afficher les matrice
        return "\n".join(["\t".join(map(str, row)) for row in self.data])    

    def __add__(self, other):
        if self.size != other.size:
            return ValueError("Les matrices doivent être de même taille pour l'addition.")
        result = Matrice(self.size)
        for a in range(self.size):
            for b in range(self.size):
                result.data[a][b] = self.data[a][b] + other.data[a][b]
        return result
    
    def __sub__(self, other):
        if self.size != other.size:
            return ValueError("Les matrices doivent être de même taille pour Soustraction.")
        result = Matrice(self.size)
        for a in range(self.size):
            for b in range(self.size):
                result.data[a][b] = self.data[a][b] - other.data[a][b]
        return result

    def __mul__(self, other):
        if self.size != other.size:
            return ValueError("Les matrices doivent être de même taille pour multiplier.")
        result = Matrice(self.size)
        for a in range(self.size):
            for b in range(self.size):
                result.data[a][b] = sum(self.data[a][b] * other.data[b][a] for f in range(self.size))
        return result

m1 = Matrice(3)
m2 = Matrice(3)

print("Matrice 1:")
print(m1)

print("\nMatrice 2:")
print(m2)

print("\nAddition des matrices:")
print(m1 + m2)

print("\nSoustraction des matrices:")
print(m1 - m2)

print("\nMultiplication des matrices:")
print(m1 * m2)