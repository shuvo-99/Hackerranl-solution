def merge_the_tools(string, k):
    # your code goes here
    while string: # AABCAAADA -> CAAADA -> ADA -> Breaks when string is empty
        s = string[0:k] # AAB -> CAA -> ADA
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:] # CAAADA -> ADA -> ''
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Alternative approach:

def merge_the_tools(string, k):
    #your code goes here
    parts = int(len(string)/ k)
    
    start = 0
    l = []
    while (start < len(string)):
        d = string[start: start + parts]
        l.append(d)
        start += parts
    
    t= ''
    
    for i in l:
        for j in i:
            if(j in t):
                pass
            else:
                t=t+j
                
        print(t)
        t=''
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
