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

14. 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
```
d1, d2 = input().split()
str(print(d2, d1))
```

15. 실수(float) 1개를 입력받아 저장한 후,
저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여
소수점 이하 둘 째 자리까지 출력하시오.
```
a = float(input())
print('%.2f'%a)
```

17. int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
```
A= int(input(''))
print(A, A, A)
```

18. 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
```
hour, minute = input().split(':')
print(hour+':'+minute)
```

19. 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
```
yyyy, mm, dd = input().split('.')
print('%04d' % int(yyyy)+'.'+'%02d' % int(mm)+'.'+'%02d' % int(dd))
```
풀이) '%04d' 는 정수를 4자리를 가져올건데 부족한자리수는 0으로 채움

20. 
주민번호는 다음과 같이 구성된다.

XXXXXX-XXXXXXX

앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
주민번호를 입력받아 형태를 바꿔 출력해보자.

```
a =input()
print(a.replace('-',''))
```

```
a, b =input().split('-')
print(a+b)
```

21. 1개의 단어를 입력받아 그대로 출력해 보자.(50자이하만 출력)

```
word = input()
if len(word) <= 50:
    print(word)
```

22. 공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력하는 연습을 해보자

```
sentense = input()
print(sentense)
```

23. 실수1개 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
```
d, f = input().split('.')
print(d)
print(f)
```

24. 단어를 1개 입력받는다. 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.

```

```

25. 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다

```

```
