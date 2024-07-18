import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 설정

# test case
T = int(sys.stdin.readline().strip())

def make_farm(M, N, K):
    farm = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        farm[Y][X] = 1
    
    return farm

def dfs(farm, x, y, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 현재 위치 방문 처리
    farm[y][x] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and farm[ny][nx] == 1:
            dfs(farm, nx, ny, M, N)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = make_farm(M, N, K)
    result = 0
    for start_y in range(N):
        for start_x in range(M):
            if farm[start_y][start_x] == 1:
                dfs(farm, start_x, start_y, M, N)
                result += 1
    print(result)
