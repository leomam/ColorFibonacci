import sys

def u(n):
    a=1
    while n != 1:
        if n%2 == 0 :
            n=n/2.0
        else :
            n=3*n+1
        a=a+1
    return a

b=40
for k in range(100000000):
    attr = []
    if(b < 47):
        b=b+1
    else:
        b=41
    attr.append(str(b))
    sys.stdout.write('\x1b[%sm%s\x1b[0m' % (';'.join(attr), str(u(k+1))))
