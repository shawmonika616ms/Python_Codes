# basket={"orange","apple","mango","apple","orange"}
# print(type(basket))
# print(basket)
# basket[0] # we cannot use this because this  set is unordered
# # another way of initialize sets
# a=set()
# a.add(1)
# a.add(2)
# print(a)

# a={}
# print(type(a))
# a={'something'}
# print(type(a))

# numbers=[1,2,3,4,5,1,2]
# unique_numbers=set(numbers)
# print(unique_numbers)
# unique_numbers.add(7)
# print(unique_numbers)

# fs=frozenset(numbers)
# print(fs)
# fs.add(5)

x={"a","b","c"}
print("a" in x)
print("g" in x)
for i in x:
    print(i)

y={"a","g","h"}
print(x|y) #union
print(x&y)# intersection
print(x-y)# difference
print(x<y) #subset output will be false because x is not subset of y
x={"h","g"}
print(x<y) # output will be true
