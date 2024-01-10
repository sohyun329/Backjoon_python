dish = list(str(input()))
high = 10

for i in range(1,len(dish)):
    if dish[i] == dish[i-1] : high += 5
    else : high += 10

print(high)