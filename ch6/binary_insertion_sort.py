# 이진 탐색 정렬 알고리즘 구하기

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

if __name__ == '__main__':
    print('선택 정렬을 수행')
    x = [6, 4, 3, 7, 1, 9, 8]

    print(x)
    binary_insertion_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')