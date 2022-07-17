# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0 
    n = len(a)
    for i in range(n - 1, 0, -1):
        print(f'패스 {n - i}')
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
        for m in range(0, n): #맨 마지막 줄
            print(f'{a[m]:2}', end='  ')
        print()
    print(f'비교를 {ccnt}번 했습니다')
    print(f'교횐을 {scnt}번 했습니다')

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