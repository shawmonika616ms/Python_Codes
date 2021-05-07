# f=open("C:\\datas\\funny.txt","a") # a for append
# f.write("\nI love mongodb")
# f.close()


# f=open("C:\\datas\\happy.txt","r")
# print(f.read()) 
# f.close()
# f=open("C:\\datas\\happy.txt","r")
# for line in f:
#     print(line)
# f.close()

# f=open("C:\\datas\\happy.txt","r")#count number of words
# for line in f:
#     tokens=line.split(' ') # split() will split the string using input character and return a list (array) of words
#     print(len(tokens))# len count the word
# f.close()

# f=open("C:\\datas\\happy.txt","r")
# f_out=open("C:\\datas\\happy_wc.txt","w")
# for line in f:
#      tokens=line.split(' ')
#      f_out.write(line+"wordcount:"+str(len(tokens)))
    
# f.close()
# f_out.close()

# if we write the below code then we don't need to close the file.
with open("C:\\datas\\happy.txt","r") as f:
    print(f.read())

print(f.closed) # this f.closed flag tells you if the file is closed or still open output is true means file is closed
