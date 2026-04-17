# def trouver_max(a, b, c) :
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     elif c>a and c>b:
#         return b
# print( trouver_max(12, 2, 2) )



# def rouver_max(name):
#     repecteur =name[0]
    
#     for element in name:
#         if element >repecteur:
#              repecteur=element
#     return repecteur

# print(rouver_max([12,36,8]))


# def nombres(liste):
#     total=0
#     for somme in liste:
#         total= total+somme

#     return total
# print(nombres([12,23,3]))


# def some(name):
#     total= 0
#     for element in name:
#         total = element+total
#     return  total

# print(some([12,23,34]))

# def est_pair(name):
    
#     for element in name:
#         if element%2==0:
#             return True
#         else:
#             return False
        

# print(est_pair([3,4,9]))

# def liste (names):
#      paire=[]
#      for elment in names:
#           if elment %2== 0:
#                paire.append(elment)
#      return paire
# print(lists([12,2,4,7]))


# def liste(names):
#     for element in names:
#         if element%2==0:
#             return True
#         else:
#             return False
# print(lists([3]))

# def summe (numbers):
#     total= 0
#     for element in numbers:
#         total=element+total
#     return(total);
# print(summe([12,23,23])

# def liste(nombres):
#     tableaux=[]
#     for element in nombres:
#         if element  not in tableaux:
#             tableaux.append(element)
#     return tableaux


# print(liste([12,23,22,22,22,22]))




# def password_valid(mdp):
    
#     for caractere in mdp:
#         if caractere.isnumeric(): 
#             return True 
            
#     return False

# # Tests
# print(password_valid("Meior"))    
# print(password_valid("Meior1234"))  


# def  cal(a,b):
#     results= a*b
#     return results
# print(cal(3,3))



def doubler_liste(nombres):
    resultat = []
    for n in nombres:
        double =n * n
        resultat.append(double)
    return resultat
print(doubler_liste([12,3,3]))