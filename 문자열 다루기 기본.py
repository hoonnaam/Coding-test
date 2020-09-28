def solution(s):
    # 길이가 4 or 6 인지 확인
    if len(s) == 4 & len(s) == 6:
        # 숫자로만 구성돼 있는지 확인
        if s.isdigit():
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer
