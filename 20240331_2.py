# 백준 10992
N = int(input())
if N == 1:
    print("*")
else:
    print(f"{' '*(N-1)}*")
    for i in range(N-2):
        print(f'{" "*(N-i-2)}*{" "*(2*i+1)}*')
    print("*"*(2*N-1))