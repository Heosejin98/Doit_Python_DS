n = int(input("n값을 입력 : ")) 
pos = [0] * n
flag_a = [False] * n    #열
flag_b = [False] * ((n * 2) - 1)   #대각
flag_c = [False] * ((n * 2) - 1)
cnt = 0

def put() -> None:
    for j in range(n):
        for i in range(n):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    global cnt
    for j in range(n):
        if (    not flag_a[j] 
            and not flag_b[i + j] 
            and not flag_c[i - j + (n - 1)]):
            pos[i] = j
            if i == (n - 1) :
                put()
                cnt += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = False
set(0)

print(f"총 조합 횟수 : {cnt}")
