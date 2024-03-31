# 백준 10951
# 틀린 답안
while True:
    user_input = input()
    if user_input != "":
        A, B = list(map(int, user_input.split(" ")))
        print(A+B)
    else:
        break

# 정답 -> try, except를 이용해라,,
while True:
    try:
        A, B = list(map(int, input().split(" ")))
        print(A+B)
    except:
        break