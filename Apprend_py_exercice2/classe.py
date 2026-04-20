class Voiture:
    voitures_crees=0
    def __init__(self,marque):
        Voiture.voitures_crees +=1
        self.marque=marque
    
Voiture_1= Voiture("Lala")
Voiture_2= Voiture("AO")
print(Voiture.voitures_crees)
