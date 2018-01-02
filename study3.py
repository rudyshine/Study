##append 和extend区别
#  a=[1,2,3]
# b=[4]
# a.append(b)##将整个列表插入到a
# print(a)
# a.extend(b)##插入列表元素
# print(a)
#
# c=[5,6,7]
# a.append(c)
# print(a)
#
# a=[1,2,3]
# a.extend(c)
# print(a)

##列表拓展方式
# import time
# def dur(op,clock):
#     duration=time.time()-clock
#     print('%s finished.Duration %.6f seconds.' %(op,duration))
#
# list1=[]
# f1=time.time()
# for i in range(1000):
#     for n in range(1000):
#         list1.append(n)
# dur('list1 appanded',f1)
#
# list2=[]
# f2=time.time()
# seq=range(1000)
# for i in range(1000):
#     list2.extend(seq)
# dur('list2 extend',f2)


# 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下 ：请将a字符串改为小写或改为大写。
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# print(a.upper())##大写
# print (a.lower())##小写