n = int(input())
a = input()
lis = a.split()
newlis = list(map(int,lis))
a_set = set(newlis)
num = int(input())
for i in range(num):
    inp = input().split(' ')
    if len(inp) == 1 and inp[0] == 'pop':
        a_set.pop()
        
    else:
        # lis = inp.split(' ')
        x,y = inp
        if x == 'remove':
            a_set.remove(int(y))
        if x == 'discard':
            a_set.discard(int(y))
        
        
print(sum(a_set))
