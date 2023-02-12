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
