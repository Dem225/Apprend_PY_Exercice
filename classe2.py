class Voiture:
    marque = "GT3 rs"
    color= "red and bleau"


voiture_01= Voiture()
voiture_02 = Voiture()
print(voiture_01.marque)
print(voiture_02.color)

Voiture.marque="Nissa"
Voiture.color= 'bleu'

print(voiture_01.marque)
print(voiture_02.color)