# 파이썬에선 진수 변환을 위한 내장함수가 포함되어 있음
# 2, 4, 8, 10, 16 진수만 있음

def solution(n):
    
    ## 10진수를 3진수로 변환
    third = ''
    while n > 0:
        div = n // 3
        mod = n % 3
        n = div
        third += str(mod)
    ## 앞뒤 반전 
    # print(third[:])
    
    ## 3진수를 10진수로 변환
    result = 0
    for idx, i in enumerate(third[::-1]):
        result += int(i) * (3 ** idx) 
    
    return result

print(solution(45))