# # book={}
# # book['tom']={
# #     'name':'tom',
# #     'address':'1 red street,NY',
# #     'phone':99989959
# # }

# # book['bob']={
# #     'name':'bob',
# #     'address':'1 green street,NY',
# #     'phone':99894783
# # }

# # import json 
# s=json.dumps(book) #it is taking dic object which is book as input thenn it is dumping it as a stirng then it will converted into a json format
# # with open("C://datas//book.txt","w") as f:
# #     f.write(s)
# f=open("C://datas//book.txt","r")
# s=f.read()
# print(s)
import json
f=open("C://datas//book.txt","r")
s=f.read()
book=json.loads(s)# this convert this book into dictionary in above case it is in string format
print(book)
print(type(book))
print(book['bob'])
print(book['bob']['phone'])

for person in book:
    print(book[person])