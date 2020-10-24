# python 정리

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
