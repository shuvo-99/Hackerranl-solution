if __name__ == '__main__':
    s = input()
    f= 0
    se=0
    t=0
    fo=0
    fi=0
    
    for i in s:
        if i.isalnum():
            f+=1
    for i in s:
        if i.isalpha():
            se+=1
    for i in s:
        if i.isdigit():
            t+=1
    for i in s:
        if i.islower():
            fo+=1
    for i in s:
        if i.isupper():
            fi+=1
            
    if f>=1:
        print(True)
    else:
        print(False)
    if se>=1:
        print(True)
    else:
        print(False)
    if t>=1:
        print(True)
    else:
        print(False)
    if fo>=1:
        print(True)
    else:
        print(False)
    if fi>=1:
        print(True)
    else:
        print(False)
