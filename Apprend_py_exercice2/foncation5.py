def find_pair_with_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1 , len(numbers)):
            if numbers[i]+numbers[j] == target:
                return [numbers[i], numbers[j]]
    return None
                
                
            
print(find_pair_with_sum([2, 0, 11, 15], 9))





# def inverse_number(n):
#     return int(str(n)[::-1])
# print(inverse_number(1234))

# def is_palindrome(word):
#     return word==word[::-1]
# print(is_palindrome("radar"))

# def count_words(sentence):
#     return len(sentence.split())
# print(count_words("Bonjour tout le monde"))


# def emove_duplicates(items):
#     lists=[]
#     for elemnt in items:
#         if elemnt not in lists:
#             lists.append(elemnt)
#     return lists

# print(emove_duplicates([1, 2, 2, 3, 1, 4]))