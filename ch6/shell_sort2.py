#셀 정렬 알고리즘 구현 (h * 3 + 1)

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j = j - h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('선택 정렬을 수행')
    #x = [6, 4, 3, 7, 1, 9, 8, 10]
    x = [8, 1, 4, 2, 7, 6, 3, 5]

    print(x)
    shell_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')
