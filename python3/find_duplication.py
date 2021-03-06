def find_duplication(ls):
    """
    n elements in ls are integers (0 to n-1)
    time complexity restriction: O(n)
    """    
    if ls == None:
        return False
    for e in ls:
        if e < 0 or e > len(ls) - 1:
            return False

    for i in range(len(ls)):     
        while ls[i] != i:           
            val = ls[i]     
            if ls[val] == val:
                return val
            ls[i], ls[val] = ls[val], ls[i]
            val = ls[i]               
    return None
 

print(find_duplication([2, 1, 3, 0, 4]))  # no duplication
print(find_duplication([2, 4, 2, 1, 4]))  # multiple duplication
print(find_duplication([2, 1, 3, 5, 4, 0, 2]))  # one duplication 
