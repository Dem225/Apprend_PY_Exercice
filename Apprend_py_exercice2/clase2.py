class Voiure:
    def __init__(self, marque):
        self.marque=marque
    def afficher_marque(self):
        print(f"LA voiture es une {self.marque}")
        
voiture1=Voiure("Lamborghini")
Voiure.afficher_marque(voiture1)