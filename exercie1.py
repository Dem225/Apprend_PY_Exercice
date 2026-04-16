def la_vie ():
    liste_de_nom = ["zebi","lobognon","manasse","lo"]
    verification = ["lObognon", "manasse","lo"]

    for element in verification:
        if element in liste_de_nom:
            return element
    
    return   "il existe personne"

resolution = la_vie()
print(resolution)