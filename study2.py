#encoding:utf-8
# ##字符串
# name='apple'
# print(name[2:])
# if name.startswith('ap'):
#     print('yes.the string starts with ap')
# if 'a' in name:
#     print('yes it contains the string a')
# if name.find('le')!=-1:##找到le
#     print('yes,it contains the string war')
#
# ## .join 列表组合成字符串
# deliminter='*^_^*'
# country=['btazil','russia','india','china']
# print(deliminter.join(country))
#
# ##序列操作（索引、切片）
# （start是切片起点索引，end是切片终点索引，但切片结果不包括终点索引的值。step是步长默认是1。）
# s_box=['pen','pencil','eraser','scissors']
# print('item 0 is',s_box[0])
# print('item 1 is',s_box[1])
# print('item 2 is',s_box[2])
# print('item 3 is',s_box[3])
# print('item -1 is',s_box[-1])
# print('item -2 is',s_box[-2])
#
# print('item 1to3 is',s_box[1:3])##1到3，不包含3
# print('item 2to end is',s_box[2:])
# print('item 1to-1 end is',s_box[1:-1])
# print('item start to end is',s_box[:])
#
# name='scissors'
# print('characters 1to3 is',name[1:3])
# print('characters 2to end is',name[2:])
# print('characters 1to-1 is',name[1:-1])
# print('characters start to end is',name[:])
# print('characters 2to7 and space is 2',name[2:7:2])##2到7 步长为2

##homework

# # b=[23,45,22,44,25,66,78]  请输出列表b中的奇数项，请最简单的方法（可考虑切片）
# b=[23,45,22,44,25,66,78]
# print(b[::2])
#
# ##str = 'This is my apple'请输出str字符串中偶数位上的字符
#
# str = 'This is my apple'
# print(str[1::2])
##对象 引用

# s_box=['apple','mango','carrot','banana']
# mybox=s_box
# del s_box[0]
# print('s_box is',s_box)
# print('mybox is',mybox)
# print('copy by naking a full slice')
# mybox=s_box[:]
# del mybox[0]
# print('s_box is',s_box)
# print('mybox is',mybox)

##例子：数字大小写
# dict_num={"0":"零","1":"壹","2":"貳","3":"弎","4":"肆","5":"伍","6":"陸","7":"柒","8":"捌","9":"玖"}
# dict_unit={0:"",1:"拾",2:"佰",3:"仟",4:"万"}
#
# flage=True
# while flage:
#     fs=[]
#     daxie=''
#     num=input('input num in (1~99999),if input q,Quit programs')
#     if num=='q'or num=='Q':
#         flage=False
#     elif int(num)<1 or int(num)>99999:
#         print('error! please input num from 1 to 99999')
#         continue
#     else:
#         listnum=list(num)##字符串转换列表
#         # print('listnum:',listnum)
#         lennum=len(listnum)-1##判断字符串个数，有几位，确定位置顺序
#         # print('lennum',lennum)
#         for item in listnum:
#             fs.append(dict_num[item]) ##获取大写
#             fs.append(dict_unit[lennum])##获取位数
#             lennum-=1
#         daxie= ''.join(fs)
#     print(daxie)

# # a=[66.25, -1, 333, 1, 1234.5, 333]
# # a.reverse()
# # print(a)
#
# stack=[3,4,5]
# stack.append(6)
# print(stack)
# print(stack.pop())