# def inverse_number(n):
#     return int(str(n)[::-1])

    
# def is_palindrome(word):
#     return word == word[::-1]

# def count_words(sentence):
#     return len(sentence.split())

# def remove_duplicates(items):
#     return list(dict.fromkeys(items)) # Préserve l'ordre original

# def find_pair_with_sum(numbers, target):
#     for elment in range(len(numbers)):
#         for listes in range(elment + 1, len(numbers)):
#             # On additionne les deux nombres pour voir si ça fait 9
#             if numbers[elment] + numbers[listes] == target:
#                 # Si c'est bon, on renvoie la paire sous forme de liste
#                 return [numbers[elment], numbers[listes]]
    
#     # Si on a fini toutes les boucles sans rien trouver :
#     return None

# # On appelle la fonction à l'extérieur (pas d'espace au début)
# print(find_pair_with_sum([2, 7, 11, 15], 9))



# def find_missing_numbers(numbers):
#     if not numbers: return []
#     n = max(numbers)
#     result = []
#     for i in range(1, n + 1):
#         if i not in numbers:
#             result.append(i)
#     return result




# def rotate_list(numbers, k):
#     k = k % len(numbers) # Pour gérer les cas où k > longueur de la liste
#     return numbers[-k:] + numbers[:-k]


# def most_frequent(numbers):
#     return max(set(numbers), key=numbers.count)


# def merge_sorted(list1, list2):
#     return sorted(list1 + list2)


# def first_unique(numbers):
#     for n in numbers:
#         if numbers.count(n) == 1:
#             return n
#     return None


# def reverse_words(sentence):
#     mots = sentence.split()
#     return " ".join(mots[::-1])


# def compress_string(s):
#     if not s: return ""
#     res = ""
#     count = 1
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             count += 1
#         else:
#             res += s[i] + str(count)
#             count = 1
#     res += s[-1] + str(count)
#     return res if len(res) < len(s) else s


# def digital_root(n):
#     while n >= 10:
#         n = sum(int(digit) for digit in str(n))
#     return n