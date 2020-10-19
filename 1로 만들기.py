def convertTo1(num):

    # 2의 배수 num % 2 == 0
    if num % 2 == 0:
        num /= 3

    # 3의 배수 num % 3 == 0
    elif num % 3 == 0:
        num /= 3

    # 2와 3의 배수가 아닐 시 빼기 1
    else:
        num -= 1

    return num


def main():
    print(convertTo1(10))


if __name__ == "__main__":
    main()
