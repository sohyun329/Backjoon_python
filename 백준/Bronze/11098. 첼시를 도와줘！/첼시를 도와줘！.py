n = int(input())
for _ in range(n):
    p = int(input())
    p_info = []
    p_name = []
    for _ in range(p) : 
        i, name = input().split()
        p_info.append(int(i))
        p_name.append(name)
    idx = p_info.index(max(p_info))
    print(p_name[idx])
    
    