n = int(input())
company = {}
for _ in range(n):
    name, state = map(str, input().split())
    company[name] = state
    if state == 'leave':
        del company[name]

sorted_company = sorted(company, reverse=True)
print('\n'.join(sorted_company))