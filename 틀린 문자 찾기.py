def findDifference(str1, str2):
    str1List = list(str1)
    str2List = list(str2)
    str1List.sort()
    str2List.sort()

    for n in range(len(str1List)):
        if str1List[n] != str2List[n]:
            return


def main():
    print(findDifference("apple", "azlppe"))


if __name__ == "__main__":
    main()
