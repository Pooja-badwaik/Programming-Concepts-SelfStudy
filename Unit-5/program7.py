def func():

    arr = [4, 1, 2, 1, 2]

    result = 0
    for num in arr:
        result = result ^ num

    print("Single number is:", result)


    



func()



def func1():


    a = 20
    b = 28

    while b != 0:
        a, b = b, a % b

    print("GCD is:", a)


func1()