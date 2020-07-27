# 이번에는 구간을 입력받고 FizzBuzz를 처리해보자.
# 두 개의 정수가 (정수) (정수) 로 입력된다.
# 5의 배수이면 Fizz, 7의 배수이면 Buzz, 5와 7의 공배수이면 FizzBuzz를 출력한다.

start, stop = map(int, input().split())
for i in range(start, stop+1):            # start부터 stop까지 확인
    if i % 5 == 0 and i % 7 == 0:         # 공배수부터 확인
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:                                 # 나머지 숫자는 그냥 
        print(i)
