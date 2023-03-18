print('hello')
单行注释#或空格开头# print("你好, 世界！")

多行注释开头结尾都是 """
"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬
"""

#2233
print('hello')


3930k
###你在他乡还好吗？

print('请输入华氏温度')
f=float(input('f='))
c=(f-32)/1.8
print('%.1f华氏度=%.1f摄氏度'%(f,c))

#从键盘输入格式 f=float(input('请输入华氏温度'))   变量=变量类型(input('提示文字'))


r=float(input('请输入圆的半径'))
l=r*3.14
a=r*r*3.14
print('周长%.2f'%l)
print('面积%.2f'%a)


import math
a=float(input('请输入第一条边长/cm\n'))
b=float(input('请输入第二条边长/cm\n'))
c=float(input('请输入第三条边长/cm\n'))
if a+b>c and b+c>a and c+a>b:
    print('这三边可以组成三角形')
    s=b+c+a
    print('周长为%.4f' % s)
    p=0.5*s
    aera=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积为%.4f' % aera)
else:
    print('这三边不能组成三角形')  
    
    
    
value0=float(input('请输入数量'))
unit=str(input('请输入单位'))
value1=float
if unit=='inch' or unit=='英寸':
    value1=2.54*value0
    print('%.2f英寸=%.2f厘米' % (value0,value1))
elif unit=='cm' or unit=='厘米' :
    value1=0.39*value0
    print('%.2f厘米=%.2f英寸' % (value0,value1))   
    
#2233
year=int(input('请输入年份'))
flag0= year%4==0 and year%100!=0 or year%400==0
print(flag0)

scores=float(input('请输入成绩'))
scores=float(input('请输入成绩'))
scores=float(input('请输入成绩'))
if scores>=90 :
    print('A')
elif scores>=80 and scores<90:
    print('B')
elif scores>=70 and scores<80:
    print('C')
elif scores>=60 and scores<70:
    print('D')
else :
    print('E')  
#2233
#233333
#23333
#莫里斯
#OSS，写下来吧
#fast
#github
#23330
#update
#23.55
#3.18 get tired there are too much car on the road
