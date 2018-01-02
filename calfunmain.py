import cafun as f
print('welcome to use claculator!')
while True:
    f.select()
    s=input('please input C,R,T,Q:')
    if s=='c' or s=='C':
        area=f.circle()
    elif s=='r' or s=='R':
        area=f.Rectangle()
    elif s=='t' or s=='T':
        area=f.Traingle()
    elif s=='q' or s=='Q':
        break
    print('the areas is:',area)
print('done')