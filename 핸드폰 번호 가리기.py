def solution(phone_number):
    # 뒤에서 5자리 수부터 *  표시 [-4:]
    front = (len(phone_number) - 4) * '*'
    end = phone_number[-4:]

    return front + end

phone_number = "01073725466"
# phone_number = "027778888"

print(solution(phone_number))

