# import argparse
# if __name__=="__main__":
#     parser = argparse.ArgumentParser()
#     args=parser.parse_args()

#positional arguments
# import argparse
# if __name__=="__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("number1",help="first number")
#     parser.add_argument("number2",help="second number")
#     parser.add_argument("operation",help="operation")
#     args=parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)
#     n1=int(args.number1)
#     n2=int(args.number2)
#     Result=None
#     if args.operation == "add":
#         Result=n1+n2
#     elif args.operation == "substract":
#         Result=n1-n2
#     elif args.operation == "multiply":
#         Result=n1*n2
#     print(Result)

    #optional arguments
# import argparse
# if __name__=="__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--number1",help="first number")
#     parser.add_argument("--number2",help="second number")
#     parser.add_argument("--operation",help="operation")
#     args=parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)
#     n1=int(args.number1)
#     n2=int(args.number2)
#     Result=None
#     if args.operation == "add":
#         Result=n1+n2
#     elif args.operation == "substract":
#         Result=n1-n2
#     elif args.operation == "multiply":
#         Result=n1*n2
#     else:
#         print("unsupported operation")
#     print(Result)


import argparse
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--operation",help="operation", choices=["add","substrac","multiply"])
    args=parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
    n1=int(args.number1)
    n2=int(args.number2)
    Result=None
    if args.operation == "add":
        Result=n1+n2
    elif args.operation == "substract":
        Result=n1-n2
    elif args.operation == "multiply":
        Result=n1*n2
    
    print(Result)