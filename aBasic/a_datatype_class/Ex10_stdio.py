"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

# -------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input('나이 입력-> '))+1
# print(age, '세입니다')
# height = eval(input('키 입력 -> '))
# print(height, 'cm')
# print(type(height))
# ----------------------------------
# 단을 입력받아 구구단을 구하기
# dan = int(input('단 입력 -> '))
# for i in range(1,10):
#     print(' {} * {} = {}'.format(dan,i,dan*i))

# -----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕', '친구', end=' ')
print('안녕' '친구')
print(1, 2, 3, 4)
for i in range(2, 8):
    print(i, end=' ')
# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3

import sys

args = sys.argv[1:4]
for i in args:
    print(i)
print('서버 연결')
