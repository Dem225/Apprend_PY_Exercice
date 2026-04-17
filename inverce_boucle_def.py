# def palindrome(prhase):
#    ranger= prhase.lower().replce(" ","")
#    inverse=""
#    for element in ranger:
#       inverse= element + inverse
#       return range==inverse
   
#    if ranger== inverse:
#       return("c'est un palindrome")
#    else:
#       return("c'est pas un palindrome")
   
# print(palindrome(["lala"]))

def palindrome(phrase):
   ranger = phrase.lower().replace(" ", "")
   inverse = ""
   
   for element in ranger:
      inverse = element + inverse
   
   if ranger == inverse:
      return "c'est un palindrome"
   else:
      return "ce n'est pas un palindrome"

print(palindrome("Laval")) 
