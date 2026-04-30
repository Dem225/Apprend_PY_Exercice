def first_unique(numbers):
   
    for i in numbers:
        if numbers.count(i)==1:
            return i
    
print(first_unique([2, 2, 3,7, 3,2]))