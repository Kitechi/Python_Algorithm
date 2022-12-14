def binary_search(lists, target):
    """Returns the index position of the target if found, else returns None"""
    first = 0
    last = len(lists)-1
    
    while first <= last:
        midpoint = (first + last) // 2
        if lists[midpoint] == target:
            return midpoint
        elif lists[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
            
    return None
        

def verify(index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("Target not found in list")
 
        
numbers = [1,2,3,4,5,6,7,8,9,10]
       
        
result = binary_search(numbers,7)
verify(result)
