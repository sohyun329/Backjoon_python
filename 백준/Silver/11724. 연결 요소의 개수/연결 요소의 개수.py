import sys
from collections import deque

sys.setrecursionlimit(10**6)  # 재귀 한도 늘리기

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
                
def count_connected_components(graph, N):
    visited = [False]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1          
    return cnt


# N: 노드의 수, M: 간선의 수
N, M = map(int, sys.stdin.readline().split())

# 그래프 정보 입력 (노드 수를 기준으로 리스트 생성)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수
cnt = count_connected_components(graph, N)
print(cnt)
