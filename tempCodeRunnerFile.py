

def rouver_max(name):
    repecteur =name[0]
    
    for element in name:
        if element >repecteur:
             repecteur=element
    return repecteur

print(rouver_max([12,36,8]))
