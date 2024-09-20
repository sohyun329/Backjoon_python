
n = int(input())
# 전체 모래양
map = [list(map(int, input().split())) for _ in range(n)]

# 누적모래
answer = 0
# 좌표 가운데 시작점
now = [n//2, n//2]

# 왼쪽 방향으로 퍼질때
left = [[-2,0,0.02],[2,0,0.02],[-1,-1,0.1],
        [-1,0,0.07],[-1,1,0.01],[0,-2,0.05],
        [1,0,0.07],[1,-1,0.1],[1,1,0.01],[0,-1,0]    
]
right = [[x,-y,z] for x,y,z in left]
up = [[y,x,z] for x,y,z in left]
down = [[-y,x,z] for x,y,z in left]

rate = {'left':left, 'right':right, 'up':up, 'down':down}

def solution(move, dx, dy, direction):
    global answer
    for _ in range(move):
        now[0] = now[0]+dx
        now[1] = now[1]+dy
        # 퍼지는 모래 양 누적(알파 값 계산)
        spread = 0
        # 회오리가 끝난 경우
        if now[0]<0 or now[1]<0:
            break
        for rx, ry, r in rate[direction]:
            nx = now[0]+rx
            ny = now[1]+ry
            # 퍼지지 않고 남은 모래
            if r == 0:
                sand = map[now[0]][now[1]]-spread
            # 비율에 따라 퍼지는 모래양
            else:
                sand = int(map[now[0]][now[1]]*r)
            # 회전 후, 범위 안에 존재한다면 모래양 누적
            if 0 <= nx < n and 0 <= ny < n :
                map[nx][ny] += sand
            # 회전 후, 범위 밖으로 퍼진 모래양 누적
            else:
                answer += sand
                
            # 퍼지지 않은 모래 양 계산을 위해 퍼진 모래 누적
            spread += sand

for i in range(n):
    if i%2 == 0:
        solution(i+1,0,-1,'left') # left
        solution(i+1,1,0,'down') # down
    else:
        solution(i+1,0,1,'right') # right
        solution(i+1,-1,0,'up') # up
        
print(answer)
        