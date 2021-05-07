# # traditional way
# numbers=[1,2,3,4,5,6,7]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
# print(even)

#list comprehension
# numbers=[1,2,3,4,5,6,7]
# even=[i for i in numbers if i%2==0]
# print(even)

# sqr_numbers=[i*i for i in numbers]
# print(sqr_numbers)

#set comprehenson

s=set([1,2,3,4,5,2,3])
print(s)



numbers=[1,2,3,4,5,6,7]
even={i for i in numbers if i%2==0}
print(even)



numbers=[1,2,3,4,5,6,7]
even={i for i in s if i%2==0}
print(even)


#list comprehension
cities=["mumbai","new york","pairs"]
countries=["india","usa","france"]
z=zip(cities,countries)
print(z)

for a in z:
    print(a)

d={city:country for city, country in zip(cities,countries)}
print(d)


