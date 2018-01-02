##运算符
# a=4
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print('This is my first program')

# a=10
# a+=10
# print(a)

##例子
##答案1
# a=input("First number:")
# b=input("second number:")
# a=int(a)
# b=int(b)
# print ("相加")
# print (a+b)
# print ("相减")
# print (a-b)
# print ("相乘")
# print (a*b)
# print ("相除")
# print (a/b)

##答案2（未调通）
# print("请选择运算")
# print ("1、相加")
# print ("2、相减")
# print ("3、相乘")
# print ("4、相除")
# o=input("These is operation")
# a=input("First number:")
# b=input("second number:")
# a=int(a)
# b=int(b)
# if o==1:
#     print(a,"+",b,"=",a+b)
#     print(print ("1、相加"))
#     c=a+b
#     print(c)
# if o==2:
#     print(a-b)
# if o==3:
#     print(a*b)
# if o==4:
#     if b!=0:
#         print(a / b)

#乘号运算符 字符与数字相乘
# print('app'*5)

##成员运算符in 或 not in
# a=[1,2,3]
# print(1 in a)
# print(5 in a )

##身份运算符 is not is
# a=3
# b=3
# print(a is b)
# print(id(a))
# print(id(b))
# c=2
# print(a is c)

#例子（求圆形面积）
# r=input('半径是：')
# r=int(r)
# pi=3.1415926
# s=pi*r**2
# print("s is ",s)

##homework 斐波那契数列,输出前十项
# f0=0
# print(f0)
# f1=1
# print(f1)
# n=2
# while n<9:
#     f2=f1+f0
#     print(f2)
#     f0=f1
#     f1=f2
#     n+=1

##控制语句判断 if 和循环while或for
##break 如果s=quit跳出程序
# while True:
#     s= input('a------->:')
#     if s=='quit':
#         break
#     print(len(s))
# print("done")

##continue
# i=0
# while True:
#     a=input('a----->:')
#     if a=='quit':
#         break#跳出程序
#     if len(a)<3:
#         print('sorry')
#         continue #跳出本次循环
#     i+=1
#     print('length of the string is:',len(a))
# print('i=',i)
# print('done!')

##猜数字(if) 只能执行一次
# num=50
# n=input('input n:')
# n=int(n)
# if n==num:
#     print('n=num')
# elif n>num:
#     print('n>num')
# else:
#     n < num
#     print('n<num')
# print('done')

##for
# num=50
# for i in range(2):
#     print('i',i)
#     guess=input('in put num:')
#     guess=int(guess)
#     if guess==num:
#         print('guess==num')
#         break
#     elif guess<num:
#         print('guess<num,lower')
#     else:
#         guess>num
#         print('guess>num,higher')
# else:
#     print('loop over')##都没猜中就结束程序
# print('done')

##while
# num=50
# flag=True
# while flag:
#     guess = input('in put num:')
#     guess = int(guess)
#     if guess==num:
#         print('guess==num')
#         flag=False##程序循环正常结束
#         # break ##直接跳出
#     elif guess<num:
#         print('guess<num,lower')
#     else:
#         guess>num
#         print('guess>num,higher')
# else:
#     print('loop over')##都没猜中就结束程序
# print('done')

##计算图形面积 圆形 长方形 三角形 退出
# flag=True#循环标志变量
# while flag:
#     print('please to select C,R,T,Q:')
#     print('C:Circle')
#     print('R:Rectangle')
#     print('T:Traingle')
#     print('Q:Quit')
#     s=input("please input:")
#     if s=='C' or s =='c':
#         r=input('please input :')
#         r=int(r)
#         ares=3.1415*r**2
#         print('the ares is:',ares)
#     elif s=='r' or s=='R':
#         l=input('please input length')
#         l=int(l)
#         w=input('please input width')
#         w=int(w)
#         ares=l*w
#         print('the ares is:',ares)
#     elif s=='t' or s=='T':
#         l=input('please input length')
#         l=int(l)
#         h=input('please input higher')
#         h=int(h)
#         ares=0.5*l*h
#         print('the ares is:', ares)
#     elif s=='q'or s=='Q':
#         flag=False
# print('done')

##honmework
#斐波那契数列（意大利语: Successione di Fibonacci)，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、……
# 在数学上，斐波纳契数列以如下被以递归的方法定义：
# F0=0，F1=1，Fn=F(n-1)+F(n-2)（n>=2，n∈N*），
# 用文字来说，就是斐波那契数列列由 0 和 1 开始，
# 之后的斐波那契数列系数就由之前的两数相加。特别指出：0不是第一项，而是第零项。
# n=int(input('please input n:'))
# f0=0
# f1=1
# # if n==1:
# #     print('f0 is:',f0)
# # elif n==2:
# #     print('f0,f1 is:',f0,f1)
# if n<2:
#     print('f0,f1 is:', f0, f1)
# else:
#     print(f0,f1)
#     # for i in range(2,n,1):
#     for i in range(n-2):
#         f2=f0+f1
#         print(f2,end=',')#关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，
#         f0=f1
#         f1=f2
# print('done')


# x=input('x')
# for x in (1,2,3):
#     print(x)


##字典值更新、添加、输出
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8;               # 更新 Age
# dict['School'] = "菜鸟教程"  # 添加信息
# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])
# print('dict len is:',len(dict))
# print(str(dict))
# print(type(dict))
# #删除字典值
# ## del dict['Name']
# ## dict.clear()
# ## del dict
# ## print(str(dict))

##

