import sys

L, C = map(int, sys.stdin.readline().split())
alphabet = sorted(list(map(str, sys.stdin.readline().split())))
comp = ['a', 'e', 'i', 'o', 'u']
key = []

def solve(start):
    if len(key) == L:
        vowel_count = sum(1 for k in key if k in comp)
        consonant_count = L - vowel_count
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(key))
        return
    
    for i in range(start, C):
        key.append(alphabet[i])
        solve(i + 1)
        key.pop()

solve(0)
