value0=float(input('请输入数量'))
unit=str(input('请输入单位'))
value1=float
if unit=='inch' or unit=='英寸':
    value1=2.54*value0
    print('%.2f英寸=%.2f厘米' % (value0,value1))
elif unit=='cm' or unit=='厘米' :
    value1=0.39*value0
    print('%.2f厘米=%.2f英寸' % (value0,value1))   