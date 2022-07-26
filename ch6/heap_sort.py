# 힙 정렬 알고리즘 구현하기

from typing import MutableMapping

def heap_sort(a: MutableMapping) -> None:
    def down_heap(a: MutableMapping, left: int, right: int)-> None:
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a) #총 길이

    for i in range((n - 1) // 2, -1, -1): # 총 길이 
        down_heap(a, i, n - 1)

    for i in range(n- 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)

if __name__ == '__main__':
    print('힙 정렬을 수행')
    x = [1, 3, 9, 4, 7, 8, 6]

    print(x)
    heap_sort(x)

    print('오름차순 정렬')
    print(x)
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')
