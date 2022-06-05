n = int(input())
arr = list(map(int,input().split()))[:n]
print(sorted(list(set(arr)))[-2])

# Alternative

i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))

# Alternative

n = int(input())
arr = input().split()[:n]
arr = [int(i) for i in arr]
arr.sort()
sort_arr = []
for i in arr:
    if i not in sort_arr:
        sort_arr.append(i)
print(sort_arr[-2])
