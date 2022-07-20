# 셀 정렬 알고리즘 구현하기

from typing import MutableSequence

def sell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0: #1칸씩 떨어진 원소까지 반복하기 위해
        for i in range(h, n): #
            j = i - h #

        
