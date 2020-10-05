# def solution(phone_number):
#     # 뒤에서 5자리 수부터 *  표시 [-5:]
#     for i in phone_number[-5::-1]:
#         table = str.maketrans('123456789', '*')
#         phone_number.translate(table)
#         print(phone_number)
#
#     return phone_number

phone_number = "01073725467"
# 연산
# for i in phone_number[0:-4]:
#     print(i)
# table = str.maketrans(', '*')
# secure_number = phone_number[:4].translate(str.maketrans('1234567890', '**********'))
secure_number = (len(phone_number) - 4) * '*'
vision_number = phone_number[6:-1]
print(secure_number)
print(vision_number)