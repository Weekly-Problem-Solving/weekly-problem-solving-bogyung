# programmers 다음 큰 숫자

def count_1(n):
    cnt = 0
    while True:
        res = n % 2
        if res == 1:
            cnt += 1
        n = n // 2
        if n == 0:
            break
    return cnt

def solution(n):
    cnt_n = count_1(n)
    for n_big in range(n+1, 1000001):
        cnt_n_big = count_1(n_big)
        if cnt_n == cnt_n_big:
            return n_big