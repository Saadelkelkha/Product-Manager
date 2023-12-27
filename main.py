from composition import Composition
from produit import Produit
from elementaire import Elementaire
from compose import Compose
from collections import namedtuple, defaultdict, deque

# Creating instances of Elementaire and Composition
p1 = Elementaire("i5", "4a5s44a", 65)
p2 = Elementaire("ram", "dfy4fdt33", 35)
co1 = Composition(p1, 20)
co2 = Composition(p2, 100)

# Creating an instance of Compose
c1 = Compose("HP", "4f3tfy", 56, 18, [co1, co2])

# Displaying information using __str__ method and other operations
print(p1)     # String representation of p1
print(p2)     # String representation of p2
print(co1)    # String representation of co1
print(co2)    # String representation of co2
print(co1 == co2)       # Equality comparison between co1 and co2
print(c1)     # String representation of c1

# Displaying the total price excluding tax for the composed product
print("Price excluding tax: ", c1.GetprixHT, "DH")

# Creating a list of products
listeproduit = [p1, p2, c1]

def afficheprix(listeproduit):
    for i in listeproduit:
        if type(i) == Elementaire:
            print("prix de", i.Getnom, "est", i.GetprixAchat)
        else:
            prix = 0
            for e in i.Getliste:
                prix += e.Getproduit.GetprixAchat
            print("prix de", i.Getnom, "est", prix)

afficheprix(listeproduit)

# Using namedtuple to represent product descriptions
Description = namedtuple('Description', ['Produit', 'Detail'])

D1 = Description(p1.Getnom, p1.__str__())
D2 = Description(p2.Getnom, p2.__str__())
D3 = Description(c1.Getnom, c1.__str__())

print("The details of product are:", D1.Detail)

# Creating a dictionary of product descriptions
des1 = {}
des1 = D1

des2 = {}
des2 = D2

des3 = {}
des3 = D3

listeDescription = defaultdict()

listeDescription[1] = des1
listeDescription[2] = des2
listeDescription[3] = des3  
print(listeDescription)

# Creating a deque of product descriptions
DeqDescription = deque()

DeqDescription.append(des1)  
DeqDescription.append(des2)  
DeqDescription.append(des3)
