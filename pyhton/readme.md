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

#### 출력 - print
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
