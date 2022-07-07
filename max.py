from typing import Any, Sequence

def max_of(a : Sequence) -> Any:
    maxinum = a[0]
    for i in range (1, len(a)):
        if(a[i] > maxinum):
            maxinum = a[i]
    return maxinum

if __name__ == '__main__':
    print('배열 최대 값')
    num = int(input('원소 갯수 입력' ))
    x = [None] * num
   
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력 :'))

    print(f'최대값 {max(x)}')   