


def SUM(n):
    if n==1 : return 1
    elif n%2==1 : return SUM(n-1) + n
    return 2*SUM(n/2) + (n/2)*(n/2)



print("결과 : " , SUM(4))

