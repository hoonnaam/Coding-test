def removeDuplicate(nums):
    result = []
    for n in range(len(nums)):
        if n == 0:
            result.append(nums[n])
        elif nums[n - 1] != nums[n]:
            result.append(nums[n])

    return result


def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8]))  # [1, 2, 5, 7, 8]을 리턴해야 합니다


def removeDuplicate(nums):
    result = []
    for n in range(len(nums)):
        if n == 0:
            result.append(nums[n])
        elif nums[n - 1] != nums[n]:
            result.append(nums[n])

    return result


def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8]))  # [1, 2, 5, 7, 8]을 리턴해야 합니다


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()