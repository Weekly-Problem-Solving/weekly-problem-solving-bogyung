from collections import Counter
S = input()
c = Counter(S.lower())
n_max = max(c.values())
max_alp = []
for alp, n in c.items():
    if n == n_max:
        max_alp.append(alp)
if len(max_alp) > 1:
    print('?')
else:
    print(max_alp[0].upper())