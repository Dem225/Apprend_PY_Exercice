def first_unique(numbers):
    lists=[]
    for i in  numbers:
        if i in lists:
            lists.append(i)
print(first_unique([1, 2, 2, 3, 3, 4]))