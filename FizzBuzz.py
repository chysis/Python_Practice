# FizzBuzz 문제의 규칙은 다음과 같다.
# 1에서 100까지 출력
# 3의 배수는 Fizz 출력
# 5의 배수는 Buzz 출력
# 3과 5의 공배수는 FizzBuzz 출력

# 두 가지 방법으로 출력해보자.

# 첫 번째 코드.
i=1
while i<=100:
    if i%3 == 0 and i%5 != 0:   # 3의 배수(이때 5의 배수는 되면 안 된다.)
        print('Fizz')
    elif i%3 != 0 and i%5 == 0: # 5의 배수(이때 3의 배수는 되면 안 된다.)
        print('Buzz')
    elif i%3 == 0 and i%5 == 0: # 3과 5의 공배수
        print('FizzBuzz')
    else:
        print(i)
    i+=1
      
# 두 번째 코드.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:         # 이것을 먼저 검사하면 3의 배수, 5의 배수에서 예외가 없다.
        print('FizzBuzz')
    elif i % 3 == 0:        # 공배수는 위에서 처리했으므로 3의 배수인지 확인
        print('Fizz')
    elif i % 5 == 0:        # 마찬가지로 5의 배수인지만 확인
        print('Buzz')
    else:
        print(i)
