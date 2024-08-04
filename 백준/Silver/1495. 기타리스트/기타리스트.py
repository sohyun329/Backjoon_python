import sys

n,s,m = map(int, sys.stdin.readline().strip().split())
v = list(map(int,sys.stdin.readline().strip().split()))

def max_volume(n,s,m,v):
    dp = [False]*(m+1)
    dp[s] = True
    
    for i in range(n):
        next_dp = [False]*(m+1)
        for j in range(m+1):
            if dp[j]:
                if j+v[i]<=m:
                    next_dp[j+v[i]] = True
                if j-v[i]>=0:
                    next_dp[j-v[i]] = True
                    
        dp = next_dp
        
    max_vol = -1
    for vol in range(m,-1,-1):
        if dp[vol]:
            max_vol = vol
            break
        
    return max_vol

print(max_volume(n,s,m,v))