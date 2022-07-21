# 셀 정렬 알고리즘 구현하기

from typing import MutableSequence

def sell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0: #1칸씩 떨어진 원소까지 반복하기 위해
        for i in range(h, n): #모든 셀 반복
            j = i - h #앞에 셀
            tmp = a[i] #뒤에 셀 값 저장
            while j >= 0 and a[j] > tmp: #앞셀이 뒷셀보다 크면
                a[j + h] = a[j] #앞셀 -> 뒷셀 (뒷셀, 뒷셀)
                j -= h
            a[j + h] = tmp #앞 셀 값 변경 (앞 셀이 더 크지 않으면 그대로)
        h //= 2 #셀 분해 1까지


if __name__ == '__main__':
    print('선택 정렬을 수행')
    #x = [6, 4, 3, 7, 1, 9, 8, 10]
    x = [8, 1, 4, 2, 7, 6, 3, 5]

    print(x)
    sell_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')


        
