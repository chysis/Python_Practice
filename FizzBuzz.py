# FizzBuzz 문제의 규칙은 다음과 같다.
# 1에서 100까지 출력
# 3의 배수는 Fizz 출력
# 5의 배수는 Buzz 출력
# 3과 5의 공배수는 FizzBuzz 출력

i=1
while i<=100:
    if i%3 == 0 and i%5 != 0: # 3의 배수(이때 5의 배수는 되면 안 된다.)
        print('Fizz')
    elif i%3 != 0 and i%5 == 0: # 5의 배수(이때 3의 배수는 되면 안 된다.)
        print('Buzz')
    elif i%3 == 0 and i%5 == 0: # 3과 5의 공배수
        print('FizzBuzz')
    else:
        print(i)
    i+=1
        
