def parlin (prhase):
    recpete = prhase.lower().replace(" ","")
    Inverse=""

    for element in recpete:
        Inverse= element + Inverse
    if recpete == Inverse:
        return("c'est un parlindrome")
    else:
        return("c'est pas un  parlindrome")
    
print(parlin("lavals"))