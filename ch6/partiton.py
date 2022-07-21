# 배열을 두 그룹으로 나누기

from typing import MutableSequence

def partition(a:MutableSequence) -> None:
    n   = len(a)
    pl  = 0
    pr  = n - 1
    x   = a[n // 2]

    while pl <= pr:
        while a[pl] < x :
            pl += 1
        while a[pr] > x :
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    print(f'피벗은 {x} 입니다.')

    print('피벗 이하인 그룹')
    print(*a[0 : pl])

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다')
        print(*a[pr + 1 : pl])
    print('피벗 이상인 그룹입니다')
    print(*a[pr + 1: n])

if __name__ == '__main__':
    print('선택 정렬을 수행')
    #x = [6, 4, 3, 7, 1, 9, 8, 10]
    x = [8, 1, 4, 2, 7, 6, 3, 5]
    #x = [1, 8, 7, 4, 5, 2, 6, 3, 9]

    print(x)
    partition(x)

