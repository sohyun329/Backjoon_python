s = str(input())

one = s.split('1')
zero = s.split('0')

res_1 = 0
res_0 = 0

for i in one:
    if '0' in i :
        res_1 += 1

for i in zero:
    if '1' in i :
        res_0 += 1

print(min(res_1, res_0))