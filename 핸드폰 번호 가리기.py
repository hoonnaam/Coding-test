def solution(phone_number):
    # 뒤에서 5자리 수부터 *  표시 [-5:]
    for i in phone_number[-5::-1]:
        table = str.maketrans('123456789', '*')
        phone_number.translate(table)
        print(phone_number)

    return phone_number