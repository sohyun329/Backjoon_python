import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 8방향 (행 변화, 열 변화)
directions = [
    (0, 0),    # 0 : X (사용 안 함)
    (0, -1),   # 1: 왼쪽 (←)
    (-1, -1),  # 2: 왼쪽 위 (↖)
    (-1, 0),   # 3: 위 (↑)
    (-1, 1),   # 4: 오른쪽 위 (↗)
    (0, 1),    # 5: 오른쪽 (→)
    (1, 1),    # 6: 오른쪽 아래 (↘)
    (1, 0),    # 7: 아래 (↓)
    (1, -1)    # 8: 왼쪽 아래 (↙)
]

# 초기 구름 위치
clouds = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]

for d, s in directions_list:
    moved_clouds = set()
    
    # 구름 이동
    for r, c in clouds:
        dd, ds = directions[d]
        nr = (r + dd * s) % N  # 행 이동 (방향 + 거리)
        nc = (c + ds * s) % N  # 열 이동 (방향 + 거리)
        
        # 물의 양 증가
        board[nr][nc] += 1
        moved_clouds.add((nr, nc))
        
    # 물복사 버그 마법
    for r, c in moved_clouds:
        cnt = 0
        for i in [2, 4, 6, 8]:  # 대각선 확인
            dr, dc = directions[i]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] > 0:
                cnt += 1
        board[r][c] += cnt
        
    # 새로운 구름 생성
    new_clouds = []
    for r in range(N):
        for c in range(N):
            # moved_clouds는 set으로 처리하여 시간 최적화
            if (r, c) not in moved_clouds and board[r][c] >= 2:
                board[r][c] -= 2
                new_clouds.append((r, c))
    
    # 다음 구름 상태로 갱신
    clouds = new_clouds

# 최종 물의 양 계산
ans = sum(map(sum, board))
print(ans)
