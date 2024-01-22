word = input()
stack = []

for _ in word :
    stack.append(word)
    word = word[1:]

for i in sorted(stack):
    print(i)