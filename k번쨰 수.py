def solution(array, commands):
    answer = []
    for i in commands:
        # 1번 항목 - 슬라이스
        new_array = array[i[0] - 1:i[1]]
        # 2번 항목 - 정렬
        new_array.sort()
        # 3번 항목 - 인덱싱
        answer.append(new_array[i[2] - 1])

    return answer


Oth = solution([2, 6, 7, 8, 4, 5, 1], [[1, 2, 1], [7, 7, 1], [3, 4, 2]])

print(Oth)