pos = [0] * 10
flag_a = [False] * 10    #열
flag_b = [False] * 19   #대각
flag_c = [False] * 19

cnt = 0

def put() -> None:
    for j in range(10):
        for i in range(10):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    global cnt
    for j in range(10):
        if (    not flag_a[j] 
            and not flag_b[i + j] 
            and not flag_c[i - j + 9]):
            pos[i] = j
            if i == 9 :
                put()
                cnt += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 9] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 9] = False
set(0)
print(f"총 조합 횟수 : {cnt}")
