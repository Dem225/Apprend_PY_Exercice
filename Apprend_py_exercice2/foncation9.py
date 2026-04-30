
# def lili(li,lie):
#     return sorted(li)==sorted(lie)


# print(lili("the", "the"))


# def merge_sorted(list1, list2):
#     lists =sorted(list1)+sorted(list2)
#     return lists


# print(merge_sorted([1, 2], [3, 4]))


def first_unique(numbers):
    for i in numbers:
        if numbers.count(i) == 1:
            return i
    return None

print(first_unique([5, 5, 6, 6, 7]) )