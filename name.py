print(__name__) #value of this variable is main. this is predefined variable in pyton, this is used like an entry point in python
def calculate_area(base,height):
    print("__name__:",__name__)
    return 1/2*(base*height)
if __name__=="__main__":
    print("I am in name.py")
    a=calculate_area(10,20)
    print("area",a)