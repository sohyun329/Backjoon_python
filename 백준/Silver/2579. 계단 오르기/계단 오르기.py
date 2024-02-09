n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0]*(n) # dp 리스트

if len(stairs) <= 2: # 계단이 2개 이하일 땐 모두 다 더해서 출력
    print(sum(stairs))
else:
    dp[0] = stairs[0] # 
    dp[1] = stairs[0]+stairs[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[-1])