list1 = [1,2.3,-35,8.9,32,117]
sum = 0 

# for i in list1:
#     sum += i

# print(sum)    

# for i in range(0,len(list1)):
#     if i % 2 == 0 :
#         sum += list1[i]

# print(sum)

# for i in list1:
#     if i % 2 == 0:
#         sum += i

# print(sum)

# for i in range(0,len(list1)):
#     if i % 2 == 0 and list1[i] % 2 == 0:
#         sum += list1[i]

# print(sum)        

# Find Max_value in list
max_val = list1[0]
# for i in list1:
#     if max_val < i:
#         max_val = i
# print(max_val)


if len(list1) > 0 :
    max_val = list1[0]
    min_val = list1[0]
    for i in list1:
        if max_val < i:
            max_val = i
        elif min_val > i :
            min_val = i    
    print(max_val)
    print(min_val)




# min_val = list1[0]
# for i in list1:
#     if min_val > i:
#         min_val = i

# print(min_val)


list1 = [1,2,5,1,7,9,10,11]

dup_list = []

for i in list1:
    if i not in dup_list:
        dup_list.append(i)
    else :
        print("Duplicates exists")    
        break