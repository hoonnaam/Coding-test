def solution(arr):
    answer = []

    for idx, number in enumerate(arr):
        # 첫번째 숫자 인덱싱
        if idx == 0:
            answer.append(number)

        # 연속적 수가 아닐 일 경우 인덱싱
        else:
            if answer[-1] != number:
                answer.append(number)

    return answer

# arr=[1,1,3,3,0,1,1]
arr=[4,4,4,3,3]

print(solution(arr))