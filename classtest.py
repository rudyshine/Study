# ##创建一个简单的类
# class Bird:
#     pass
# bird= Bird()##对类进行实例化
# print(bird)

##方法的调用
# class Bird:
#     def hi(self):
#         print('hello i am bird !')
# bird= Bird()##对类进行实例化
# print(bird.hi())##调用hi的方法

# ##类的初始化
# class Bird:
#     ##初始化语句
#     def __init__(self, name):
#         self.name = name
#
#     def hi(self):
#         print('hello i am bird,name is !', self.name)
#
# bird = Bird('sparrow')
# print(bird.hi())


##例子
class Bird:
    number=0
    def __init__(self,name):
        self.name=name
        print(('Initializing %s')%self.name)
        Bird.number+=1

    def __del__(self):
        print(('%s said bye')%self.name)
        Bird.number-=1
        if Bird.number==0:
            print('i am the last one')
        else:
            print('There are still %d birds left'%Bird.number)

    def sayHi(self):
        print('Hi i am a lovely bird,name is %s'%self.name)

    def howMany(self):
        if Bird.number==1:
            print('i am the only bird here.')
        else:
            print('we have %d birds here.'%Bird.number)

    def eating(self):
        print('i am eating,chirp...')

sparrow=Bird('sparrow')
sparrow.sayHi()
sparrow.howMany()

cuckoo=Bird('Cuckoo')
cuckoo.sayHi()
cuckoo.howMany()

sparrow.howMany()
print(Bird.sayHi.__doc__)

