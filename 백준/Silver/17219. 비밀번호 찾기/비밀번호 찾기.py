n, m = map(int, input().split())

site = {}

for _ in range(n):
    s, pw = map(str, input().split())
    site[s] = pw

search_pw = []
    
for _ in range(m):
    ss = input()
    if ss in site:
        search_pw.append(site[ss])

print('\n'.join(search_pw))