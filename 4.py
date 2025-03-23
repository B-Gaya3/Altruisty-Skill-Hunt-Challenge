def minswap(n, a, b):
    if sorted(a) != sorted(b):
        return -1
    
    a = list(a)
    b = list(b)
    swaps = 0
    
    for i in range(n):
        if a[i] != b[i]:
            j = i
            while a[j] != b[i]:
                j += 1
         
            while j > i:
                a[j], a[j-1] = a[j-1], a[j]
                swaps += 1
                j -= 1
    
    return swaps

n = int(input())
a = input().strip()
b = input().strip()

print("Output")
print(minswap(n, a, b))
