def find_pair_with_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1 , len(numbers)):
            if numbers[i]+numbers[j] == target:
                return [numbers[i], numbers[j]]
    return None
                
                
            
print(find_pair_with_sum([2, 0, 11, 15], 9))


def find_pair_with_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i +1,len(numbers)):
            if numbers[i] +numbers[j]==target:
                return [numbers[i],numbers[j]]
    return None

print(find_pair_with_sum([2, 0, 1111, 15], 9))