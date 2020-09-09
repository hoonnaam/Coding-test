def solution(arr):
    if len(arr) == 1:
        arr[0] = -1
    else:
        arr.remove(min(arr))
    return arr
arry = [10,6,8,5,2,3]
print(solution(arry))
arry = [1000000000]
print(solution(arry))