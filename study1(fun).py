# ##没有参数
# def helloword():
#     print('hello')
#     # return 'hell0'
# helloword()#调用函数
# # print(helloword())

##形参a、实参x(实参x值传递给形参a)
# def number(a,b):
#     if a%2==0:
#         print('this is an even number')
#     else:
#         print(b)
#         print('this is an odd number')
#
# if __name__ == '__main__':
#     x=int(input('please input number'))
#     y='odd number'
#     number(x,y)

##局部变量和全局变量是针对作用域
##局部变量
# def fun(x):
#     print('x is',x)
#     x=2 ##内部变量，不影响外部变量
#     print('change x is ',x)
#
# x=50
# fun(x)
# print('x still is',x)

##全局变量 global （不推荐使用）
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
# fun1()

##默认参数
# def eat(dessert,fruit='apple'):
#     print('i like',dessert)
#     print('i like',fruit)
# #调用函数
# eat('chocolate')##第二个参数fruit使用默认参数
# eat('icecream','banana')
# ##含有默认值的参数不能放在不含有默认值参数的前面,比如：
# # def eat(fruit='apple',dessert):

##关键参数
# def func(a,b=5,c=10):
#     print('a is:',a,'and b is:',b,'and c is:',c)
# func(3,7)
# func(8,c=24) ##c=24为关键参数,b取默认
# func(c=50,a=100)##位置不重要，b取默认值

##return
# def num(x):
#     return x*2
# print(num(5))

# #没有写return的，会默认返回None
# def hi():
#     print('hello word')
# print(hi())
#
# ##文档字符串
# def hi():
#     'this is a simple example!'
#     print('hello word')
# hi()
# print(hi.__doc__)

##计算图形面积 圆形 长方形 三角形 退出
# def circle():
#     r = int(input('please input :'))
#     ares = 3.1415 * r ** 2
#     return ares
# def Rectangle():
#     l = int(input('please input length'))
#     w = int(input('please input width'))
#     ares = l * w
#     return ares
# def Traingle():
#     l = int(input('please input length'))
#     h = int(input('please input higher'))
#     ares = 0.5 * l * h
#     return ares
#
# flag=True#循环标志变量
# while flag:
#     print('please to select C,R,T,Q:')
#     print('C:Circle')
#     print('R:Rectangle')
#     print('T:Traingle')
#     print('Q:Quit')
#     s=input("please input:")
#     if s=='C' or s =='c':
#         ares=circle()
#
#     elif s=='r' or s=='R':
#         ares=Rectangle()
#
#     elif s=='t' or s=='T':
#         ares=Traingle()
#     elif s=='q'or s=='Q':
#         flag=False
#     print('the ares is',ares)
# print('done')

##homework
##请运用函数的思想编写判断输入的年份是否为闰年。
# 其中闰年的判断标准如下：
# 非整百年数除以4，无余为闰，有余为平；\
# 整百年数除以400，无余为闰有余平
##方案一
# def year(x):
#     print(type(x))
#     if x%400==0 and x%100==0:
#         print('leap year',x)
#     elif x%100!=0 and x%4==0:
#         print('average year',x)
#     else:
#         print('average year',x)
# x = int(input('pleass input year'))
# year(x)

##方案二return
# def leap(x):
#     if x % 100 != 0 and x % 4 == 0:
#         return True
#     elif x%400==0 and x%100==0:
#         return False
#     else:
#         return False
#
# year=int(input('please input year:'))
# if leap(year):##调用函数
#     print('This is leap year!')
# else:
#     print('This is average year!')

# ##模块
# import sys
# print('the command line arguments are:')
# for i in sys.argv:
#     print(i)
#

##calfunmain.py 引用cafun模块
##cafun.py

##homework
# import time
# list1=[]
# list2=[]
# start=time.time()
# for i in range(1000):
#     for n in range(1000):
#         list1.append(n)
# print(time.time()-start)
# print(start)
#
# start=time.time()
# seq=range(1000)
# for i in range(1000):
#     list2.extend(seq)
# print(time.time()-start)
# print(start)

##数据结构（列表/元组/）
##列表
# s=['1','2','3']
# ##列表操作
# s_box=['pen','pencil','eraser','scissors']
# print('i have',len(s_box),'items.')
# print('there item are:')
# for item in s_box:##遍历s_box
#     print(item,end=',')#打印item
# print('i also have to buy glue')
# s_box.append('glue')##末尾增加
# print('now i have',s_box)
# print('i will sort my list now')
# s_box.sort()##排序（按字母顺序排序）
# print('sorted list is',s_box)
# print('the first item i have is',s_box[0])
# olditem=s_box[0]##把s_box[0]的值符给临时变量
# del s_box[0]#删除
# print('i lost the',olditem)##打印删除的元素
# print('now i have',s_box)

##元组（值不可以改变）
# a=(1,2,3)
# del a[0]##元组对象不支持元素修改
##元组打印练习
# garden=('rose','azalea','mum')
# print('number of flowers in the garden is',len(garden))
# new_garden=('peony','orchid',garden)#garden在这里是元组
# print('number of flowers in the new garden is',len(new_garden))
# print('all flowers in new garden are',new_garden)
# print('flowers brought from old garden are',new_garden[2])
# print('last flower brought from old garden is',new_garden[2][2])

# num=15
# a='apple'
# name='zhang'
# print('%s have %d %s'%(name,num,a))#用%加元组的形式打印

#字典（键值对）
# ab={'zhang':'123@','wang':'213','huang':'456','zhao':'654'}
# print(len(ab))
# print('huang address is %s'%ab['huang'])
# ab['ye']='789'
# print(len(ab))
# del ab['wang']
# print('there are %d contacts in the address-book'%len(ab))
# for name,address in ab.items():
#     print('contacts %s at %s'%(name,address))
#     if 'wang'in ab:
#         print('huang address id %s'%ab['wang'])##已经删除无法打印了

