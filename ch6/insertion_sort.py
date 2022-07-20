# 단순 삽입 정렬 알고리즘 구현

from typing import MutableSequence

def insertiont_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        tmp = a[i]
        for j in range(i, -1, -1):
            if a[j - 1] > tmp:
                a[j] = a[j - 1]
            else:
                break
        a[j] = tmp

if __name__ == '__main__':
    print('삽입 정렬을 수행')
    x = [6, 4, 3, 7, 1, 9, 8]

    print(x)
    insertiont_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')