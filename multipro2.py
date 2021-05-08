# import time
# import multiprocessing
# # here each time we will get the different value hence we need locking
# def deposit(balance):
#     for i in range(100):
#         time.sleep(0.01)
#         balance.value =balance.value+1

# def withdraw(balance):
#     for i in range(100):
#         time.sleep(0.01)
#         balance.value = balance.value-1

# if __name__ == '__main__':
#     balance = multiprocessing.Value('i',200)
#     d = multiprocessing.Process(target=deposit,args=(balance,))
#     w = multiprocessing.Process(target=withdraw,args=(balance,))
#     d.start()
#     w.start()
#     d.join()
#     w.join()

#     print(balance.value)


import time
import multiprocessing

def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()                         # critical section
        balance.value =balance.value+1         # critical section
        lock.release()                         # critical section

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value-1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit,args=(balance, lock))
    w = multiprocessing.Process(target=withdraw,args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()

    print(balance.value)
