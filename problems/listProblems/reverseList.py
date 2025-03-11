# List reverse without using built-in methods

def reverse_list(my_list):
    # If the list is empty or has only one element
    if len(my_list) <= 1:
        return my_list

    n = len(my_list)

    for i in range(0, n // 2):
        temp = my_list[i]
        my_list[i] = my_list[n - i - 1]
        my_list[n - i - 1] = temp

    return my_list


print("Reversed List:", reverse_list([1, 2, 3, 4, 5]))    
print("Reversed List:", reverse_list([1, 2, 3, 4]))       
print("Reversed List:", reverse_list([1]))                
print("Reversed List:", reverse_list([]))                  
print("Reversed List:", reverse_list([5, 4, 3, 2, 1]))    
print("Reversed List:", reverse_list([1, 1, 1, 1, 1]))    
print("Reversed List:", reverse_list([-1, -2, -3, -4]))    
print("Reversed List:", reverse_list([1, -2, 3, -4]))   