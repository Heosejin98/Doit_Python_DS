# Doit_Python_DS

## 자료구조 배열
### 1. list 
*  뮤터블 list (변경가능)
* list 생성방법
    * list = [] 
* list를 생성 할려면 반드시 원소의 개수를 결정해야된다 
    * list = [None] * numeber None을 이용하여 원솟값을 정하지 않은 리스트 생성가능
### 2. tuple
* 이뮤터블 자료형 (변경불가)
* tuple 생성방법
    * tuple01 = ()


###  3. **시퀀스 자료형이란?**

파이썬에선 아래 이미지와 같이 각각의 요소들이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence types) 라고 합니다. (bytes 와 bytearray 도 있습니다)

![sequence](./img/sequence.png)

파이썬에서는 각각의 값들을 요소(element) 라고 부릅니다.
시퀀스 자료형으로 만든 객체를 시퀀스 객체라고 하며, 각각의 값이 요소 입니다.

## 4. ****파이썬3 함수에서 ‘→’, ‘:’, ‘=’****

```jsx
def funName(x: str, y: float = 6.5) -> int:
    return x + y

value = funName(3)
print(value)
```

**함수명 : def 다음에 나와있는 funName**

- funName의 리턴 값의 형식을 지정 해 줄 때 →로 지정한다.
- x : str         콜론(:) 다음에 적어주는 것은 매개변수에 할당되는 형식을 말한다.
- y : float = 6.5 초기값을 콜론다음에 해당 형식 뒤에 = 하고 값을 적어줄 수 있다. (변수 : 형식 = 기본값)

## **5. 파이썬 타입 어노테이션**

파이썬은 3.5 버전부터 타입 어노테이션을 지원하기 시작한다. 다만 정적 언어에서와 같은 적극적인 타입 체크가 아니라 **타입 어노테이션**(type annotation), 즉 타입에 대한 힌트를 알려주는 정도이다. 동적 언어의 장점을 잃지 않고 기존에 작성된 코드와의 호환성을 생각하면 당연한 선택일 것이다.

타입 어노테이션은 다음과 같이 사용한다.

```python
num: int = 1
```

변수명 바로 뒤에 : int와 같이 사용하여 num 변수가 int형임을 명시한다.

```python
defadd(a: int, b: int) -> int:
return a+b
```

함수의 매개변수에도 같은 규칙을 적용하여 매개변수의 타입을 명시할 수 있다. 그리고 함수의 반환값도 `-> 타입`처럼 사용하여 반환값의 타입을 명시할 수 있다.

> 어노테이션 타입으로 정수는 int, 문자열은 str, 리스트는 list, 튜플은 tuple, 딕셔너리는 dict, 집합은 set, 불은 bool을 사용한다.
> 

## 6. 모듈

파이썬에서는 하나의 스크립트를 모듈이라고 한다

- [파일명].py에서 [파일명]은 하나의 모듈 이름으로 사용된다.
    - ex) 파일명이 max.py라면 max는 모듈 명이 된다.
- 다른 파일에서 from [모듈명] improt[함수명] 으로 호출 가능

### 필요한 모듈만 가져오기

파이썬에서 임포트를 하는 방법 두 가지

첫 번째 방법:

```python
import 모듈
```

두 번째 방법:

```python
from 모듈import 이름
```

1. 첫번째 방법은 모듈 전체를 가져오구요
2. 두번째 방법은 모듈 내에서 필요한 것만 콕 찍어서 가져오는 방법이죠. 

두 방법을 비교

```python
>>>import tkinter
>>> tkinter.widget = tkinter.Label(None, text='I love Python!')
>>> tkinter.widget.pack()

```

첫 번째 방법으로 모듈을 불러오면 모듈 내의 변수를 사용하기 위해서는 `모듈.변수`의 형식으로 써줘야함

```python
>>>from tkinterimport *
>>> widget = Label(None, text='I love Python!')
>>> widget.pack()
```

두 번째 방법은 모듈내의 이름을 콕 찍어서 가져오는 방법인데, 위에서는 `tkinter`에 있는 것을 전부(`*`) 가져왔습니다. 이렇게 하면 좀 더 편리하군요.

하지만 마냥 좋기만 한 방법은 아니랍니다. 아래의 예에서는 문자열이었던 `Label`이 임포트 문 실행 후 `tkinter`의 `Label`로 바뀌어 버린 것을 볼 수 있습니다.

```python
>>> Label = 'This is a Label'
>>>from tkinterimport *
>>> Label
<class 'tkinter.Label'>
```
## 7. for - else 문이 작동되는 과정

- for문과 같이 사용되는 else문
    - for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우 
    else문이 실행되는 방식으로 진행됩니다.

```python
cnt = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        cnt += 1
        if n % prime[i] == 0 : 
            break
    else : ##for-else
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
    
print(f'총 연산 횟수 : {cnt}')
```

소수를 판별하는 알고리즘에서 현재 값이 이전 소수까지 나눴을때 끝까지 연산된다면 n을 새로운 소수로 판별