from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None :

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None :
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center: #버퍼에 값 복사
                buff[p] = a[i]
                p += 1
                i += 1
        
            while i <= right and j < p: 
                if buff[j] <= a[i]: 
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

 
    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff


if __name__ == '__main__':
    print('merge sort 수행')
    x = [8, 1, 4, 2, 7, 6, 3, 5]

    merge_sort(x)

    print('오름차순 정렬') 
    print(x)