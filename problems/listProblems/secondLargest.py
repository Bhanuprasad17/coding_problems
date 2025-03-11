def find_second_largest(my_list):
    if len(my_list) < 2:
        return "Second Largest Number: Not Found"
    
    largest = my_list[0]
    second_largest = float('-inf')

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] > second_largest and my_list[i] != largest:
            second_largest = my_list[i]

    if second_largest == float('-inf'):
        return "Second Largest Number: Not Found"
    else:
        return second_largest


my_list = [10, 2, 5, 6, 12, 9]
print("Second Largest:", find_second_largest(my_list))

my_list = [1, 5, 2, 10, 9]
print("Second Largest:", find_second_largest(my_list))

my_list = [3, 3, 3, 3, 3]
print("Second Largest:", find_second_largest(my_list))

my_list = [5]
print("Second Largest:", find_second_largest(my_list))

my_list = []
print("Second Largest:", find_second_largest(my_list))
