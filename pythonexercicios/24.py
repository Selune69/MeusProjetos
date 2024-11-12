n = int(input())
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)

#or

n = int(input())
ans = {i : i * i for i in range(1, n+1)}
print(ans)