# python 정리
 * 참고 : https://wikidocs.net/

## 사용자 입출력
### 입력 - input
 * input은 입력되는 모든 것을 문자열로 인식
``` python
>>> a = input("입력하세요. : ")
this is test.
>>> a
"this is test."
```

### 출력 - print
 * 콤마는 띄어쓰기로 인식
```
>>> print("this", "is", "test")
this is test
```
 * 한줄에 여러 결과 출력
```
>>>for i in range(10):
       print(i, end=' ')
0 1 2 3 4 5 6 7 8 9
 ```



## 파일 입출력
```
f = open("새파일.txt", 'w') // 파일명, 파일 모드(r, w, a) a는 파일 마지막 부분에 내용 추가
line = f.readline()
allLine = f.read()
f.write("test")
f.close()
```

### sys 모듈로 매개변수 입력
`test.py aaa bbb ccc` 에서 aaa, bbb, ccc를 변수로 받으려면
```
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```

## 자료형
#### 리스트
```
>>> a = [1, 3, 5, 7]
>>> a[0:2]
[1, 3]
>>> del a[1] //a.remove(3) <- 리스트에 있는 첫번째 3을 삭제
>>> a
[1, 5, 7]
```
#### 튜플
 * 리스트는 항목의 값 변경이 가능하지만 튜플은 불가능하다.
```
>>> t1 = (1, 3, 'b')
>>> t1[2]
'b'
```
#### 딕셔너리
```
>>> dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}`
>>> dic[name]
pey
```
### 집합 set
 * 중복 없고 순서도 없다.
 * 교집합 `&`, 합집합 `|`, 차집합 `-` 사용 가능
```
>>> s2 = set("Hello")
>>> s2
{'e', 'H', 'l', 'o'}
```
### 값 복사하기
```
>>> a = [1,2,3]
>>> b = a
>>> a is b
true

>>> a = [1, 2, 3]
>>> b = a[:]
>>> a[1] = 4
>>> a
[1, 4, 3]
>>> b
[1, 2, 3]
```

## 함수
 * 입력될 파라미터가 몇개인지 모를 경우
 ```
def 함수이름(*매개변수):  // 매개변수에 변수가 리스트로 들어옴.
    <수행할 문장>
    ...
 ```

## 클래스
 * 파이썬 메서드의 첫번째 매개변수는 관례적으로 self(인스턴스 그 자체)
 ```
 >>> class FourCal:
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
...
>>> a = FourCal();
>>> a.setdata(4, 2) // FourCal.setdata(a, 4, 2)도 가능
```
#### 생성자 : `__init__`
 * 객체 생성 시점에 자동 호출
```
def __init__(self, first, second):
    self.first = first
    self.second = second
```

## 모듈
 * `import mod1` 
    * mod1 모듈의 모든 함수 사용 가능. mod1.함수명으로 사용
 * `from mod2 import add` 
    * mod2 모듈에서 add 함수만 사용 가능. `mod2.` 붙일 필요없이 add 로만 사용 가능. 
 * `if __name__ == "__main__":` 의 의미
    * 해당 문장 아래 있는 실행 내용들은, 해당 문장이 있는 모듈을 직접 실행할 경우에만 실행된다.
    * 모듈로 import 할때는 실행되지 않을 내용들을 넣을때 사용됨.