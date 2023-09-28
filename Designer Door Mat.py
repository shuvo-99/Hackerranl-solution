num = input().split(' ')
n=int(num[0])
m=int(num[1])
dash = '-'
list1=[]
if n%2 !=0: 
  if (n>5 and n<101) and (m>15 and m<303):
    for i in range(n):
      
      if i >= (n//2)+1:
        print(list1.pop())

      elif i == (n//2):
        mid_text = 'WELCOME'
        total_dash = m - len(mid_text)
        half_dash = int(total_dash/2)
        print(dash*(half_dash)+mid_text+dash*(half_dash))

      else:
        mid = '.|.'*int(2*i+1)
        mid_len = len(mid)
        total_dash = m - mid_len
        half_dash = int(total_dash/2)
        print(dash*(half_dash)+mid+dash*(half_dash))
        a=dash*(half_dash)+mid+dash*(half_dash)
        list1.append(a)
