t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    z=list(map(int,input().split()))
    m=x[1]+x[2]+y[2]
    n=y[0]+z[0]+z[1]
    if(m>n):
        print(m)
    else:
        print(n)