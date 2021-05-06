d={"tom":12345, "rob":6789, "joe":45566}
print(d)
print(d["tom"])
d["sam"]=987654321
print(d)
del d["sam"]
print(d)
for key in d:
    print("key",key,"value",d[key])
for k, v in d.items():
    print("key",key,"value",v)
print("tom" in d)
print("samir" in d)
d.clear()
print(d)
#tuples
point=(5,9)
print(point[0])
print(point[1])
point[0]=50#error because tuple is immutable