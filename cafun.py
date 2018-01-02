def main():
    print('this is program is being run by itself')


if __name__ == '__main__':
    main()
else:
    def select():
        print('please to select C,R,T,Q:')
        print('C:Circle')
        print('R:Rectangle')
        print('T:Traingle')
        print('Q:Quit')

    def circle():
        r = int(input('please input :'))
        ares = 3.1415 * r ** 2
        return ares


    def Rectangle():
        l = int(input('please input length'))
        w = int(input('please input width'))
        ares = l * w
        return ares


    def Traingle():
        l = int(input('please input length'))
        h = int(input('please input higher'))
        ares = 0.5 * l * h
        return ares