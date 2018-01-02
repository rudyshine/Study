#用python实现输入年显示对应的生肖，输入月、日显示星座。
# 已知1972年是鼠年，只要可以查1972年以后的就行了。


def get_zodiac(year):
    index=(year-1972)%12
    return get_zodiac(index)

def get_constellatin(month,date):
    dates={20,19,21,20,21,22,23,23,23,24,23,22}
    constellatin={'摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座',
                  '狮子座','处女座','天枰座','天蝎座','射手座','摩羯座'}
    if date<dates[month-1]:

        return constellatin[month-1]
    else:
        return  constellatin[month]

zodiac={0:'鼠',1:'牛',2:'虎',3:'兔',4:'龙',5:'蛇',6:'马',7:'羊',8:'猴',9:'鸡',10:'狗',11:'猪'}
t=input('please input year month date(1972-01-01):')
listtime=t.split('-')##去掉字符串的链接符，并换成列表
year=int(listtime[0])
month=int(listtime[1])
date=int(listtime[2])


print('you zodiac is:',get_zodiac(year))
print('you cinstellatin is:',get_constellatin(month,date))