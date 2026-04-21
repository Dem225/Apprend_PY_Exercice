
def are_anagrams(word1, word2):
    lists1=[]
    lists2=[]
    for i in word1:
        lists1.append(i)
    for j in word2:
        lists2.append(j)
    if sorted(lists1)==sorted(lists2):
        return True
    else:
        return False
    
print(are_anagrams("hello", "world"))
