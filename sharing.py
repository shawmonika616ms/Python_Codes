# import time
# import multiprocessing
# square_result=[]


# def calc_square(numbers):
#     global square_result
#     for n in numbers:
#         print('square' +str(n*n))
#         square_result.append(n*n)
#     print(" within a process :result" +str(square_result))



#sharing data by array
# if __name__== "__main__":
#     arr = [2,3,8,9]
#     p1= multiprocessing.Process(target=calc_square,args=(arr,))

#     p1.start()
#     p1.join()
#     print("result" +str(square_result))
#     print("Done!")

# import multiprocessing

# def calc_square(numbers,result):
#     for idx, n in enumerate(numbers):
#         result[idx]=(n*n)
  
# if __name__ == "__main__":
#     numbers =[2,3,5]
#     result=multiprocessing.Array('i',3)
#     p=multiprocessing.Process(target=calc_square,args=(numbers,result))

#     p.start()
#     p.join()

#     print(result[:])


#sharing data by value
import multiprocessing

def calc_square(numbers,result,v):
    v.value=5.67
    for idx, n in enumerate(numbers):
        result[idx]=(n*n)
  
if __name__ == "__main__":
    numbers =[2,3,5]
    result=multiprocessing.Array('i',3)
    v= multiprocessing.Value('d',0.0)
    p=multiprocessing.Process(target=calc_square,args=(numbers,result,v))

    p.start()
    p.join()


    print(v.value)