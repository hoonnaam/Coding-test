def convertTo1(num):

    # count = 0
    # while num != 1:
    #     # 2의 배수 num % 2 == 0
    #     if num % 3 == 0:
    #         num /= 3
    #
    #     # 3의 배수 num % 3 == 0
    #     elif num % 2 == 0:
    #         num /= 2
    #
    #     # 2와 3의 배수가 아닐 시 빼기 1
    #     else:
    #         num -= 1
    #
    #     count += 1
    #
    # return count

    dp = [0 for _ in range(num + 1)]

    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1

    return dp[num]


def main():
    print(convertTo1(20))


if __name__ == "__main__":
    main()
