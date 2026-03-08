

def func1():

    num = int(input("Enter a number: "))
    flag = True

    if num <= 1:
        flag = False
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

    if flag:
        print("Prime number")
    else:
        print("Not a prime number")


func1()


def func2():
        

        
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        max_num = max(a, b)

        while True:
            if max_num % a == 0 and max_num % b == 0:
                lcm = max_num
                break
            max_num += 1

        print("LCM is:", lcm)




func2()