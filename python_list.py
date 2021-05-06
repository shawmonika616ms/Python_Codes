items=["bread","pasta","fruits","veggies"]
print(items)
print(items[0])
items[0]="butter"
print(items)#list are mutable inpython
print(items[0:2])
print(items[-1])
items.append("chips")
print(items)
items.insert(1,'chips')
print(items)


food=["bread","pasta","fruits"]
bathroom=["shampoo","soap"]
item=food+bathroom
print(item)
print(len(item))

print("bread" in item)
print("soda" in item)