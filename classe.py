class Voiture:
    marque = "Lamborghini"
    couleur= "rouge"
    

Voiture0_2= Voiture()
print(Voiture0_2.couleur)

Voiture.marque="toyotal"

Voiture0_1 = Voiture()
print(Voiture0_1.marque)


Voiture0_1.marque='ffff'
Voiture0_2.marque='erz'
print(Voiture0_1.marque)