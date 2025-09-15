import array as my_array

x = list(range(0,100,3))
arr = my_array.array('i',x)

#slicing
arr0=arr[10:20]
for i in range(len(arr0)):
    print(arr0[i],end=" ")
print('\n')
#negative indexing
arr1=arr[10:-10]
for i in range (len(arr1)):
    print(arr1[i],end=" ")
print('\n')
arr2 = arr[: : -1]
for i in range(len(arr2)):
    print(arr2[i],end=" ")