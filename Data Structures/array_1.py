
# num=[1,3,4,5,6]

# #INSERTION

# num.insert(1,2)
# print(num)

# #append
# num.append(7)
# print(num)

# #extend
# num.extend([8,9])
# print(num)

# #DELETION

# num.remove(1)
# print(num)

# # num.pop()
# print(num)

# num.pop(2)
# print(num)

# num.clear()
# print(num)

 #TRAVERSAL

# num1 = [1,2,3,4,5,6,9]
# for i in range(len(num1)):
#     print(i)

# for i in num1:
#     print(i)

#LINEAR SEARCH
def linear_search(arr,value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i
    return -1

num=[1,2,3,4,5]
to_find = 2

res=linear_search(num,to_find)
print(res)