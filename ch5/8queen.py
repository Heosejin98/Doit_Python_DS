pos = [0] * 8
flag_a = [False] * 8    #열
flag_b = [False] * 15   #대각
flag_c = [False] * 15
cnt = 0

def put() -> None:
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    global cnt
    for j in range(8):
        if (    not flag_a[j] 
            and not flag_b[i + j] 
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7 :
                put()
                cnt += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False
set(0)
print(f"총 조합 횟수 : {cnt}")
