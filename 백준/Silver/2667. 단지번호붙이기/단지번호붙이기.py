import sys

# 지도 크기
N = int(sys.stdin.readline().strip())

# 지도 정보 입력
map_info = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# DFS 구현
def dfs(x, y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[x][y] = 0  # 방문 처리
    cnt = 1  # 현재 위치 포함

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            cnt += dfs(nx, ny, graph)

    return cnt

# 각 단지의 아파트 수를 저장할 리스트
info = []

# 지도 정보를 순회하며 DFS 탐색 시작
for x in range(N):
    for y in range(N):
        if map_info[x][y] == 1:
            info.append(dfs(x, y, map_info))

# 결과 출력
print(len(info))
for i in sorted(info):
    print(i)