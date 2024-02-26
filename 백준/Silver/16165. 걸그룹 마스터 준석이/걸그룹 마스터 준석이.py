n, m = map(int, input().split())

group = {}
answer = []

for _ in range(n):
    team = input()
    num = int(input())
    group[team] = []
    for _ in range(num):
        member = input()
        group[team].append(member)
    group[team].sort()
    
for _ in range(m):
    quize = input()
    target = int(input())
    if target == 0:
        answer.extend(group[quize])
    else:
        for key, value in group.items():
            if quize in value:
                answer.append(key)
                
for ans in answer:
    print(ans)