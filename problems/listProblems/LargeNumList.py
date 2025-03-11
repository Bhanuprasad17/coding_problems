# Large number in list

def find_large_num(my_list):

    if len(my_list) == 0:
        return "List is empty, no minimum element."
    
    if len(my_list) == 1:
        return my_list[0]
    
    large_num = my_list[0]

    for i in range(1,len(my_list)):
        if  large_num < my_list[i] :
            large_num = my_list[i]

    return large_num


print("Test Case 1:", find_large_num([10, 2, 5, 6, 12, 9]))    
print("Test Case 2:", find_large_num([5]))
print("Test Case 3:", find_large_num([]))                     
print("Test Case 4:", find_large_num([3, 3, 3, 3, 3]))        
print("Test Case 5:", find_large_num([-10, -5, -2, -100, 0]))  
print("Test Case 6:", find_large_num([5, 5, 5, 5, 10, 5]))    
print("Test Case 7:", find_large_num([-5, -2, 0, 3, 7]))    
print("Test Case 8:", find_large_num([9, 10, 11, 12, 1]))   
print("Test Case 9:", find_large_num([2, 1, 3, 4, 5]))      
print("Test Case 10:", find_large_num([10, 20, 30, 5, 4]))    
print("Test Case 11:", find_large_num([-10, -20, -30, -5]))    
print("Test Case 12:", find_large_num([100000, 99999, 88888]))  
print("Test Case 13:", find_large_num([-100000, -99999, -88888])) 
print("Test Case 14:", find_large_num([10, 10, 10, 10]))      
print("Test Case 15:", find_large_num([1, 5, 10, 2, 10]))

