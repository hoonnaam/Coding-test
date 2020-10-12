def twoSum_plus(nums, target):
    # 하나의 nums가 target 보다 크다면 pass
    nums.sort()
    # for idx, i in enumerate(nums):
    #     if i > target:
    #         nums = nums[:idx]

    # 두 nums의 합이 target 가 일치하는지
    for i in range(len(nums)):
        for p in (range(len(nums) - 1)):
            if nums[i] + nums[p + 1] == target:

                # 일치한다면 두 nums 출력
                return nums[i], nums[p + 1]

    # 효율성을 높이기 위한 함수 수정 반복문2회 -> 1회
    i = 0
    j = len(nums) - 1

    while i < j:
        sum = nums[i] + nums[j]
        if sum == target:
            return nums[i], nums[j]
        elif sum < target:
            i += 1
        else:
            j -= 1

def main():
    print(twoSum_plus([2, 8, 19, 37, 4, 5, 9, 13], 12))


if __name__ == "__main__":
    main()
