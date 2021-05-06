'''tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

total=0
for item in tom_exp_list:
    total=total+item
print("Tom's total expense:",total)

total=0
for item in joe_exp_list:
    total=total+item
print("Joe's total expense:",total)'''

'''def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total
tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

toms_total=calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)

print("toms total expenses", toms_total)
print("joe total expenses",joe_total)'''




# def sum(a,b):
#     total=a+b
#     return total

# # n=sum(6,5)
# # print("total",n)
# n=sum(b=6,a=5) #named argumenst
# print("total",n)

# total=0
# def sum(a,b):
#     total=a+b
#     print("total inside function",total)
#     return total


# n=sum(b=6,a=5) 
# print("total outside function",total)

total=0
def sum(a,b=2):#default arguments
    total=a+b
    print("total inside function",total)
    return total


n=sum(5,8)
"""
Docstrings
"""
print("total outside function",total)