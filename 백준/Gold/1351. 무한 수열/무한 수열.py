N, P, Q = map(int, input().split())

dict = {}
dict[0] = 1

def dfs(N):
    # n번째 값이 저장되어있다면, 그대로 반환
    if (N in dict):
        return dict[N]
    # n번째 값이 저장되어 있지 않다면, n번째 값을 계산 및 저장한 뒤, 반환
    else:
        dict[N] = dfs(N//P) + dfs(N//Q)
        return dict[N]
print(dfs(N))