n = int(input())

plus = []
minus = []

result = 0

for _ in range(n):
    num = int(input())
    if num > 1 :
        plus.append(num)
    elif num <= 0 :
        minus.append(num)
    else:
        result += num
        
plus.sort(reverse=True) #내림차순
minus.sort() #오름차순

#양수묶기
for i in range(0,len(plus),2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i]*plus[i+1])

#음수묶기
for i in range(0, len(minus),2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i]*minus[i+1])

print(result)