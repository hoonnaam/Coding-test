def solution(s):
    c_word = ""
    n = 0
    for alpa in s:
        # print(alpa)
        if alpa == ' ':
            c_word += alpa
            n=0
        else:
            if n % 2 ==0:
                c_word += alpa.upper()
            else:
                c_word += alpa.lower()
            n += 1
    return c_word

string = "try  hello world"

print(solution(string))