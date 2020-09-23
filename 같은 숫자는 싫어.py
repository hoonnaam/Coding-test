def solution(arr):
    answer = []
    for idx, number in enumerate(arr):
        # 첫번째 숫자 인덱싱
        if idx == 0:
            answer.append(number)

        # 연속적 수가 일 경우 인덱싱
        else:
            if arr[idx] == arr[idx+1]:
                answer.remove(number)

        print(answer)

        # 연속적 수가 아닐 경우 제거print('Hello Python')
        return answer