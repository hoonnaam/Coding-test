def isAnagram(str1, str2):
    # 배열 이용

    # 	str1List = list(str1)
    # 	str2List = list(str2)
    # 	str2List.sort()
    # 	str1List.sort()

    # return (str2List == str1List)

    # 해시 사용
    dic1 = {}
    for n in str1:
        dic1[n] = dic.get(n, 0) + 1

    for p in str2:
        if p in dic1:
            if dic1[p] == 0:
                return False
            else:
                dic1[n] -= 1
        else:
            return False
    return True


def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle'))  # should return True
    print(isAnagram('cat', 'cap'))  # should return False


if __name__ == "__main__":
    main()
