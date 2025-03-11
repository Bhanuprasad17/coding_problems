# List reverse without using built-in methods

my_list = [1,2,3,4,5]

n = len(my_list)

for i in range(0,n//2):
    # my_list[i],my_list[n-i-1] = my_list[n-i-1],my_list[i]
    temp = my_list[i]
    my_list[i] = my_list[n-i-1]
    my_list[n-i-1] = temp

print(my_list)    