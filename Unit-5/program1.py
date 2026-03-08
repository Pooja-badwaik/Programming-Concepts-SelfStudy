# 1. Explain any two sorting algorithms and write their Python programs.

def func():

    arr = [5, 2, 9, 1, 3]

    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print("Sorted array:", arr)


func()


def func1():

    arr = [5, 2, 9, 1, 3]

    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted array:", arr)



func1()