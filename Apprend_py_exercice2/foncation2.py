#     return word==word[::-1]

# print(is_palindrome("radar"))

# def is_palindrome(word):
#     return word==word[::-1]


# def count_words(sentence):
#     return len(sentence.split())
# print(count_words("Bonjour tout le monde"))

# def remove_duplicates(items):
#     respeteur=[]
#     for elment in items:
#         if elment not in respeteur:
#             respeteur.append(elment)
#     return respeteur
# print(remove_duplicates([1, 2, 2, 3,3, 1, 4]))

# def find_pair_with_sum(numbers, target):
#     for elment in range(len(numbers)):
#         for indice in range(elment+1,len(numbers)):
#             if numbers[elment]+numbers[indice] == target:
#                 return [numbers[elment],numbers[indice]]
# print(find_pair_with_sum([2, 7, 11, 15], 9))


# def max(t):
#     max = t[0]
#     for i in t:
#         if i > max:
#             max = i
#     return max



# def find_missing_numbers(numbers):
#     n = max(numbers)
#     lists=[]
#     for i in range(1,n+1):
#         if i not in numbers:
#             lists.append(i)
#     return lists

# print(find_missing_numbers([2, 3, 7,100009 ,2,8]))