year=int(input('请输入年份'))
flag0= year%4==0 and year%100!=0 or year%400==0
print(flag0)