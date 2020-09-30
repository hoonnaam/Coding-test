def solution(seoul):
    answer = ''
    # "Kim"이 몇번째에 있는지 확인
    for idx, p in enumerate(seoul):
        if p == "Kim":
            x = idx
    answer = f'김서방은 {x}에 있다'
    print(type(answer))

    return answer

seoul = ["Jane", "Michle", "Kim"]
print(solution(seoul))

# def findKim(seoul):

#     return "김서방은 {}에 있다".format(seoul.index('Kim'))