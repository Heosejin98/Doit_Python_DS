# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0 
    n = len(a)
    for i in range(n - 1, 0, -1):
        print(f'패스 {n - i}')
        exchange = 0
        for j in range(0, i, 1):
            for m in range(0, n): #패스의 한행 
                print(f'{a[m]:2}' + ('  'if m != j else #비교하는 부분이 아니면 (공백) 
                                    ' -' if  a[j + 1] > a[j] else '->'), # 바뀌면 -> 안바뀌면 -
                                    end='')
            print()
            ccnt += 1
            if  a[j] > a[j + 1]:
                scnt += 1
                a[j + 1], a[j] = a[j], a[j + 1]
                exchange += 1
        for m in range(0, n): #맨 마지막 줄
            print(f'{a[m]:2}', end='  ')
        print()
        if exchange == 0:
            break
    print(f'비교를 {ccnt}번 했습니다')
    print(f'교환을 {scnt}번 했습니다')

 
if __name__ == '__main__':
    print('버블 정렬을 수행')
    x = [6, 4, 3, 7, 1, 9, 8]

    print(x)
    bubble_sort(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')