# 버블 정렬 알고리즘 구현하기
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1, 0, -1):
        for j in range(0, i, 1):
            if  a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
 
if __name__ == '__main__':
    print('버블 정렬을 수행')
    x = [6, 4, 3, 7, 1, 9, 8]

    print(x)
    bubble_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')