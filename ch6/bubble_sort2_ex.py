# [Do it! 실습 6-3] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 1) - 정렬 과정을 출력

from typing import MutableSequence

def bubble_sort2_verbose(a: MutableSequence) -> None:
    """버블 정렬(교환 횟수에 따른 중단)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f"패스 {i + 1}")
        exchng = 0  # 패스에서의 교환 횟수
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(
                    f"{a[m]:2}"
                    + ("  " if m != j - 1 else " +" if a[j - 1] > a[j] else " -"),
                    end="",
                )
            print(f"{a[n - 1]:2}")
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        for m in range(0, n - 1):
            print(f"{a[m]:2}", end="  ")
        print(f"{a[n - 1]:2}")
        if exchng == 0:  # 교환이 수행되지 않았으면 작업을 중단
            break
    print(f"비교를 {ccnt}번 했습니다.")
    print(f"교환을 {scnt}번 했습니다.")

if __name__ == '__main__':
    print('버블 정렬을 수행')
    x = [6, 4, 3, 7, 1, 9, 8]

    print(x)
    bubble_sort2_verbose(x)

    print('오름차순 정렬')
    for i, value in enumerate(x):
        print(f'x[{i}] = {value}')