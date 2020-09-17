def solution(array, commands):
    answer = []
    for i in range(3):
        seq = commands[i]
        # 1번 항목
        new_array = array[seq[0] - 1:seq[1]]
        # 2번 항목
        new_array.sort()
        # 3번 항목
        answer.append(new_array[seq[2] - 1])

    return answer


solution([2, 6, 7, 8, 4, 5, 1], [[1, 2, 1], [7, 7, 1], [3, 4, 2]])