def para(word1,word2):
    lists1=word1.split()
    liste2=word2.split()
    l1=[]
    l2=[]
    for i in lists1[0]:
        l1.append(i)
    for j in liste2[0]:
        l1.append(j)
    if l1.sort()==l2.sort():
        return True

   
        


print(para("hello", "world"))





def para(word1, word2):
    l1 = []
    l2 = []
    
    # On met chaque lettre de word1 dans l1
    for i in word1:
        l1.append(i)
        
    # On met chaque lettre de word2 dans l2
    for j in word2:
        l2.append(j)
        
    # On compare les deux listes TRIÉES
    if sorted(l1) == sorted(l2):
        return True
    else:
        return False

print(para("hello", "world")) # Affiche False
print(para("niche", "chien")) # Affiche True