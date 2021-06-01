arr=[56,89,1,2,7,9,6,6,2,3,1,4,5,6,8,9,9,9,5,54,56,89,7,1,2]
# key should be element
# value should be frequency if element present in that arr
mydictionary = dict()
for element in arr:
    if element not in mydictionary:
        #first occurenece initialize frequency with 1
        mydictionary[element]=1
    else:
        mydictionary[element]+=1
print(*arr)
print(arr.sort)
print(*arr)
print(mydictionary)
