x = input()
size = input().split(' ')

# convert size into int
size = [int(i) for i in size]

customer_num = int(input())
shoe_size=[]
money = []
add = 0

for i in range(customer_num):
    pl, sl = input().split(' ')
    shoe_size.append(pl)
    money.append(sl)
    
# convert shoe_size into int    
shoe_size = [int(i) for i in shoe_size]
# convert money into int
money = [int(i) for i in money]

for j in range(0,len(shoe_size)):
    if shoe_size[j] in size:
        add = add + money[j]
        size.remove(shoe_size[j])
print(add)
