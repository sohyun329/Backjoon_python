import sys
input = sys.stdin.readline

n = int(input().rstrip())
flowers = []
for _ in range(n):
    sm, sd, em, ed = list(map(int, input().rstrip().split()))
    flowers.append([sm * 100 + sd, em * 100 + ed])

flowers.sort()
end = 301
cnt = 0

while flowers:
    if (end > 1200) or (end < flowers[0][0]): #더 안봐도 되거나 현재 보는 꽃이 더 늦게 피는 경우
        break
    #직전에 핀 꽃과 현재 피는 꽃이 연결되어 있음
    temp = -1
    for _ in range(len(flowers)):
        if end >= flowers[0][0]:
            if temp <= flowers[0][1]:
                temp = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    end = temp
    cnt += 1

if end < 1201:
    print(0)
else:
    print(cnt)