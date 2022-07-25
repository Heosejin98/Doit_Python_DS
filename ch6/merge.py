from typing import Sequence, MutableSequence

def merge_sort_list(a: Sequence, b: Sequence, c:MutableSequence) -> None:
    pa, pb, pc = 0, 0, 0 #각 배열의 주소
    na, nb = len(a), len(b) #각 배열의 길이

    while pa < na and pb < nb : #두 개 다 각 배열만큼 크면 
        if a[pa] <= b[pb]: #b가 더 크면
            c[pc] = a[pa]
            pa += 1
        else :
            c[pc] = b[pb]
            pb += 1
        pc += 1
    
    while pa < na :
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    while pb < nb :
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    print('선택 정렬을 수행')
    a = [2, 4, 6, 8, 11 ,13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))

    merge_sort_list(a, b, c)

    print('오름차순 정렬')
    for i, value in enumerate(c):
        print(f'x[{i}] = {value}')
