from collections import deque

def minmaxbright(k, n, brightness):
    if k > n:
        return -1
    
    dq = deque()
    max_values = []

    for i in range(k):
        while dq and brightness[dq[-1]] <= brightness[i]:
            dq.pop()
        dq.append(i)
    
    for i in range(k, n):
        max_values.append(brightness[dq[0]])
   
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and brightness[dq[-1]] <= brightness[i]:
            dq.pop()
        dq.append(i)

    max_values.append(brightness[dq[0]])
   
    return min(max_values)

k = int(input())
n = int(input())
brightness = [int(input()) for _ in range(n)]
print("Output")
print(minmaxbright(k, n, brightness))
