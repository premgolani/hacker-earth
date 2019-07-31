t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=a.count(a[0])
    if (c%2==0):
        print('Unlucky')
    else:
        print('Lucky')

