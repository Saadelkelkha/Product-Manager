import copy

class Composition:
    def __init__(self, produit, quantite):
        # Copy the produit object to ensure independent instances
        self.__produit = copy.copy(produit)
        self.__quantite = quantite
    
    @property
    def Getproduit(self):
        # Getter for produit attribute
        return self.__produit
    
    @property
    def Getquantite(self):
        # Getter for quantite attribute
        return self.__quantite
    
    def Setproduit(self, p1):
        # Setter for produit attribute
        self.__produit = p1

    def Setquantite(self, q):
        # Setter for quantite attribute
        self.__quantite = q

    def __str__(self):
        # String representation of the object
        return f"product: {self.__produit.__str__()}   ;  quantity: {str(self.Getquantite)};  "

    def _eq_(self, other):
        # Equality comparison based on produit and quantite attributes
        return (self.Getproduit == other.Getproduit) and (self.Getquantite == other.Getquantite)
