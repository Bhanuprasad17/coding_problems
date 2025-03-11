# Min Number in the list

def minNumList(my_list):

    if len(my_list) == 0:
        return "List is empty, no minimum element."
    
    if len(my_list) == 1:
        return my_list[0]
    
    min_num = my_list[0]

    for i in range(1,len(my_list)):
        if  min_num > my_list[i] :
            min_num = my_list[i]

    return min_num


print("Minimum Element:", minNumList([10, 2, 5, 6, 12, 9]))     
print("Minimum Element:", minNumList([5]))                      
print("Minimum Element:", minNumList([]))                      
print("Minimum Element:", minNumList([3, 3, 3, 3, 3]))          
print("Minimum Element:", minNumList([-10, -5, -2, -100, 0])) 
print("Minimum Element:", minNumList([5, 5, 5, 5, 1, 5]))      
print("Minimum Element:", minNumList([-5, -2, 0, 3, 7]))       
print("Minimum Element:", minNumList([9, 10, 11, 12, 1]))     
print("Minimum Element:", minNumList([2, 1, 3, 4, 5])) 