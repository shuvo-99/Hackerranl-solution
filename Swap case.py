def swap_case(s):
    res =''
    for i in s:
        if i.isupper():
            res += i.lower()
        elif i.islower():
            res += i.upper()  
        else:
            res +=i
    return res
if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)
