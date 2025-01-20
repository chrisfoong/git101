start = 0
lst = [int(e) for e in input().split()]

result = 0

for i in range(len(lst)):
    
    # if start < lst[i]:
    #     for j in range(start, lst[i]):
    #         result += j + 1
    #     start = lst[i]
    # else:
    #     for j in range(lst[i], start):
    #         result += j + 1
    #     start = lst[i]

    # if start < lst[i]:
    #     m,n = start,lst[i]
    # else:
    #     m,n = lst[i], start
    m = min(start, lst[i])
    n = max(start, lst[i])

    for j in range(m, n):
        result += j + 1
    start = lst[i]

print(result)