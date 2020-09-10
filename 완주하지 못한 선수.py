def solution(participant, completion):
    # p = participant
    completion.sort()
    participant.sort()
    p = participant
    c = completion
    for idx in range(len(c)):
        if p[idx] != c[idx]:
            return p[idx]
    return p[len(p)-1]

players = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(players, completion))