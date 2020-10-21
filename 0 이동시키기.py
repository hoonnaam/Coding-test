def moveZerosToEnd(nums):
    leng = nums.count(0)
    for n in range(leng):
        # 0인 인덱스 제거
        nums.remove(0)
        # 0인 인덱스 삽입
        nums.append(0)

    return nums


def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))


if __name__ == "__main__":
    main()
