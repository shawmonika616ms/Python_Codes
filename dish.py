indian=["samosa","daal","naan"]
chinese=["egg","pot sticker","fried-rice"]
italian=["pizza","pasta","risotto"]
dish=input("Ente a dish name")

if dish in indian:
     print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("Italian")
else:
    print("I don't know which cuisine is this",dish)
