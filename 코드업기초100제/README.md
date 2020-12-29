### 코드업 기초 100제

1. Hello 출력하기
```
print('Hello')
```
2. Hello World
```
print('Hello World')
```
3.
Hello

World
```
print('Hello\nWorld')
```
4. 'Hello'
```
print("'Hello'")
```

5. "Hello World"
```
print('"Hello World"')
```
6. "!@#$%^&*()"
(단, 큰따옴표도 함께 출력한다.)
```
print('"!@#$%^&*()"')
```
7. "C:\Download\hello.cpp"
(단, 큰따옴표도 함께 출력한다.)
```
print('"C:\\Download\\hello.cpp"')
```
8.
┌┬┐

├┼┤

└┴┘
```
print("\u250c\u252c\u2510\n\u251c\u253c\u2524\n\u2514\u2534\u2518")
```
10. 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후
변수에 저장되어 있는 값을 그대로 출력해보자.
```
a = int(input(''))
print(a)
```
11. 문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후
변수에 저장되어 있는 문자를 그대로 출력해보자.
```
a = str(input(''))
print(a)
```
12. 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후
저장되어 있는 실수값을 출력해보자.
```
a=float(input())
print('%.6f'%a)
```
(소수점 이하 자릿수 지정 : '%.자릿수f'%숫자)

13. 정수(int) 2개를 입력받아 그대로 출력해보자.
```
a, b = input().split()
x = int(a)
y = int(b)
print(x, y)
```
split 함수를 통해 공백을 기준으로 하여 a와 b로 나누어 주어서 확실하게 정수로 받기위해서 int를 통해 
각각을 x와 y로 저장을 해주고 출력을 한다.
