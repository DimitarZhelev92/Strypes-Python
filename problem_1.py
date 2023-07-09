def getMin(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = min(res, arr[i])
    return res

def getMax(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = max(res, arr[i])
    return res

def sum_of_min_and_max(arr, n):
    min = getMin(arr, n)
    max = getMax(arr, n)
    return min + max


arr = [ -10,5,10,100 ]
n = len(arr)

print("Sum = " , sum_of_min_and_max(arr, n))