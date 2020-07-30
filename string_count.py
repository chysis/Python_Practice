# 표준 입력으로 문자열이 들어오면 그 문자열에서 특정 단어(특수문자 제외)가 몇 번 나왔는지 세는 프로그램
# 아래의 예시에서는 'the'의 개수를 찾는다.

# 입력된 문자열을 공백을 기준으로 split하여 리스트에 저장하고,
# 각각의 문자 양쪽의 특수문자를 제거한 뒤 카운트하는 방법을 이요했다.


# CODE 
import string

s=input().split(' ')
for i in range(len(s)):
    s[i]=s[i].strip(string.punctuation)
n=s.count('the')
print(n)
