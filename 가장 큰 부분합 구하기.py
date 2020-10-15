def maxSubArray(nums):

    result = []
    # 반복문을 통해 슬라이싱
    for n in range(len(nums)):
        for p in range(len(nums)):
            result.append(sum(nums[n:p + 1]))

    return max(result)


def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]))  # 30이 리턴되어야 합니다


if __name__ == "__main__":
    main()