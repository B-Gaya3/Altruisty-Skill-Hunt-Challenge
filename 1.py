def maxprofit(p):
    if len(p)<=1:
        return 0
    minp=p[0]
    maxp=0
    for i in p[1:]:
        if i<minp:
            minp=i
        else:
            maxp = max(maxp,i-minp)

    return maxp

n=int(input("Enter the number of days:"))
print("Enter the stock prices separated by spaces")
p=list(map(int,input().split()))
print(maxprofit(p))
