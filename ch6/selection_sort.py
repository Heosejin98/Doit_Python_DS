#단순 선택 정렬 알고리즘

from typing import MutableSequence

def select_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

if __name__ == '__main__':
    print('선택 정렬을 수행')
    x = [6, 4, 3, 7, 1, 9, 8]

    print(x)
    select_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')