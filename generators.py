# def remote_control_next():
#     yield "cnn"
#     yield "espn"
# itr=remote_control_next()
# print(itr)
# print(next(itr))
# print(next(itr))

# for c in remote_control_next():
#     print(c)


# febonaccci series using generators

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>50:
        break
    print(f)