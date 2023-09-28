# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = input()
lis = a.split()
newlis = list(map(int, lis))
a_set = set(newlis)
n = int(input())
b = input()
lis = b.split()
newlis = list(map(int, lis))
b_set = set(newlis)

a_b = a_set.difference(b_set)
b_a = b_set.difference(a_set)

order_lis = []
for i in a_b:
    order_lis.append(i)
for i in b_a:
    order_lis.append(i)
order_lis.sort()
for i in order_lis:
    print(i)
