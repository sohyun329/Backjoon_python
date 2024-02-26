import sys
input = sys.stdin.readline

def move(i, j, di, dj):
    return warp(i+di, N), warp(j+dj, M)

def warp(i, N):
    if i < 0 :
        return N-1
    elif i >= N:
        return 0
    return i

def recur(s, ni, nj, w):
    if dd.get(w) == None:
            dd[w] = 1
    else:
        dd[w] += 1

    if s == 4:
        return

    for di, dj in delta:
        i, j = move(ni, nj, di, dj)
        if (ni != i or nj != j):
            recur(s+1, i, j, w+arr[i][j])    

N, M, K = map(int, input().split())

arr = [input().rstrip() for _ in range(N)]

dd = {}
delta = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1),(-1,1)]

for i in range(N):
    for j in range(M):
        recur(0, i, j, arr[i][j])

for _ in range(K):
    s = input().rstrip()
    if dd.get(s) == None:
            print(0)
    else:
        print(dd[s])