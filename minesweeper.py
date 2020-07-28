# 표준 입력으로 가로와 세로가 입력되고 그 다음 줄부터 문자가 입력된다.
# '.'는 지뢰가 아니고, '*'는 지뢰이다.

# 예를 들어

# 3 3
# .**
# *..
# .*.

# 가 입력된다면 .에 인접한 지뢰의 개수를 출력한다.

# <결과>
# 2**
# *43
# 2*1

col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

# fill 0 in matrix
for i in range(row):
    for j in range(col):
        if matrix[i][j] != '*':
            matrix[i][j] = 0

# search mine | 주위 8칸에서의 지뢰를 찾는다.
mine = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] != '*':                                       # 지뢰가 없는 칸에만 값을 입력
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or y < 0 or x > row - 1 or y > col - 1:  # 영역을 벗어나는 경우
                        continue                                      # 찾는 것을 건너뛴다
                    else:
                        if matrix[x][y] == '*':
                            mine += 1
            matrix[i][j] = mine
            mine = 0


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='')
    print()
