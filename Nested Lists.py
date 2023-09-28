num = int(input())
list1 = []
val_list=[]

for i in range(num):
    name = input()
    value = float(input())
    val_list.append(value)
    list1.append([name,value])

val_list.sort()
val_list=list(dict.fromkeys(val_list))
elem = val_list[1]
name_list = []

for i in list1:
  if i[1] == elem:
    name_list.append(i[0])

name_list.sort()

for i in name_list:
    print(i)
