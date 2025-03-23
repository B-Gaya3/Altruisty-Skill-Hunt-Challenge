def count(s, queries):
    n=len(s)
    psum=[0]*(n+1)
    for i in range(n):
        psum[i+1]=psum[i]+(1 if s[i] == 'T' else 0)
    res=[]
    for start, end in queries:
        res.append(psum[end]-psum[start-1])
    return res

s=input().strip()
n=int(input())
q=[tuple(map(int, input().split())) for _ in range(n)]
for res in count(s, q):
    print(res)
