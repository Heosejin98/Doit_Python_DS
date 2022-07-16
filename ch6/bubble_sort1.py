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
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}] = "))

    print(x)
    bubble_sort(x)

    print('오름차순 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')