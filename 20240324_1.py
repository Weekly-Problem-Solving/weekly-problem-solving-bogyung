# 백준 
S = input()
result = ''
for alp in 'abcdefghijklmnopqrstuvwxyz':
    if alp in S:
        result += str(S.index(alp))
        result += ' '
    else:
        result += '-1 '
print(result[:-1])