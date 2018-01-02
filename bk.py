# ##文件备份方案一
# import time,os
#
# source=['/home/390646/PycharmProjects/study','/home/390646/过程版本/jdbk']##源
# target_dir='/home/390646/PycharmProjects/BK_crawl'##备份到的地址
#
# today=target_dir+time.strftime('%y%m%d')+time.strftime('%H%M%S')##备份目录+获取当前时间
#
# target=today+'.rar'##备份后的文件名
# for i in range(len(source)):##若有多个备份路径会循环执行备份命令
#     rar_command="rar a %s -r %s "%(target,source[i])
#     ##对文件进行压缩 （压缩命令为rar a表示创建压缩文档的命令；第一个%s为源目录；-r为递归所有文件并进行压缩；第二个%s为备份路径）
#     if os.system(rar_command)==0:##系统去运行rar命令
#         print('Successfull backup to',target)
#     else:
#         print('backup failed')

##文件备份方案二（备份的文件在当前目录并以当前日期创建文件夹）
import time,os

source=['/home/390646/PycharmProjects/study','/home/390646/zzz/jdbk']##源
target_dir='/home/390646/bk/'##备份到的地址

today=target_dir+time.strftime('%y%m%d')##备份目录+获取当前时间
now=time.strftime('%H%M%S')
target=today+'/'+now+'.rar'##备份后的文件名

if not os.path.exists(today):##判断是否存在文件夹
    os.mkdir(today)
    print('Successfully created directory',today)

for i in range(len(source)):##若有多个备份路径会循环执行备份命令
    rar_command="rar a %s -r %s "%(target,source[i])
    ##对文件进行压缩 （压缩命令为rar a表示创建压缩文档的命令；第一个%s为源目录；-r为递归所有文件并进行压缩；第二个%s为备份路径）
    if os.system(rar_command)==0:##系统去运行rar命令
        print('Successfull backup to',target)
    else:
        print('backup failed')


#文件备份方案二（备份的文件在当前目录并以当前日期创建文件夹，并增加文档描述部分）
# import time,os
#
# source=['/home/390646/PycharmProjects']##源
# target_dir='/home/390646/bk/'##备份到的地址
#
# today=target_dir+time.strftime('%y%m%d')##备份目录+获取当前时间
# now=time.strftime('%H%M%S')
# comment=input('Please input comment:')
#
# if comment=='':
#     target=today+'/'+now+'.rar'##备份后的文件名
# else:
#     target=today+'/'+now+'_'+comment.replace(' ','_')+'.rar'
#     #comment.replace('','_')若用户输入空格则用下划线代替
# if not os.path.exists(today):##判断是否存在文件夹
#     os.mkdir(today)
#     print('Successfully created directory',today)
#
# for i in range(len(source)):##若有多个备份路径会循环执行备份命令
#     rar_command="rar a %s -r %s "%(target,source[i])
#     ##对文件进行压缩 （压缩命令为rar a表示创建压缩文档的命令；第一个%s为源目录；-r为递归所有文件并进行压缩；第二个%s为备份路径）
#     if os.system(rar_command)==0:##系统去运行rar命令
#         print('Successfull backup to',target)
#     else:
#         print('backup failed')
