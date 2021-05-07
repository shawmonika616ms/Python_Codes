#print(1/0)
#print('abc'+2)

# Handling Exception
# x=input("Enter the number1")
# y=input("Enter the number2")
# try:
#     z=int(x)/int(y)
# except Exception as e:
#     print("Exception occured",e)
#     z=None
# print("Division:",z)

x=input("Enter the number1")
y=input("Enter the number2")
try:
    z= x/int(y)
except ZeroDivisionError as e:
    print("divison by zero xception",e)
    z=None
except Exception as e:
    print('exception type:', type(e).__name__)
    z=None
print("Division:",z)