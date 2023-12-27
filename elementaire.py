from produit import Produit  # Importing the Produit class from the module produit

class Elementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        # Constructor to initialize attributes
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    @property
    def GetprixAchat(self):
        # Getter for prixAchat attribute
        return self.__prixAchat
    
    def SetprixAchat(self, prixAchat):
        # Setter for prixAchat attribute
        self.__prixAchat = prixAchat

    def __str__(self):
        # String representation of the object
        return f"{super().__str__()}  Purchase price: {str(self.GetprixAchat)}"

    def GetprixHT(self):
        # Delegating the GetprixHT method to the superclass (Produit)
        return super().GetprixHT()
