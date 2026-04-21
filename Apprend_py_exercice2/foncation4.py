def remove_duplicates(items):
    lists=[]
    for element in items:
        if element not in lists :
            lists.append(element)
    return lists
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
        