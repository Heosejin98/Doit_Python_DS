# 비재귀적인 퀵 정렬 구현하기

from stack import Stack
from typing import MutableSequence

def quick_sort(a: MutableSequence, left: int, right: int) -> None:
    range = Stack(right - left + 1)
    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = a[(left + right) // 2]

        while pl <= pr:
            while a[pl] < x :
                pl += 1
            while a[pr] > x :
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr:
            range.push((left, pr))
        if pl < right:
            range.push((pl, right))

def qsort(a: MutableSequence) -> None:
    quick_sort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print('선택 정렬을 수행')
    #x = [6, 4, 3, 7, 1, 9, 8, 10]
    x = [8, 1, 4, 2, 7, 6, 3, 5]

    print(x)
    qsort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')
