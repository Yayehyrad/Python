def sum(a, b):
    """simple function that adds to int"""
    return a+b

# print(sum(1,2))
# help(sum)
"""Zip(dic1,dic2) => val : val
    enumerate(dic) => index : value
"""
item1 = ['new' , "old"]
item2 = [43 , 23]
 
# for index , name ,num in  enumerate(zip(item1, item2)):
#     print(index , name , num )
# mylist = [ 10 if x%2 == 0 else 0 for x in range(1,10)  ]

# print(mylist)
arr = [1,2,3,4,5]

print(list(map(lambda x : x**2 , arr)))