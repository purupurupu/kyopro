import sys
import copy


###### 標準入力一覧 ######
s = input()
n = int(input())

# 【1行】n文字
# abc def ghi
a, b, c = input().split()  # 3個の文字列の入力を受け取る
str_list = list(input().split())  # n個の文字列がリストに格納される

# 【1行】n数字
# 1 2 3
a, b, c = map(int, input().split())  # 3個の数字の入力を受け取る
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

# 【n行】1文字
# 3
# aa
# a
# aaa
n = int(input())  # nは入力回数
str_list = [input() for _ in range(n)]

# 【n行】1数字
# 4
# 2
# 3
# 4
# 5
n = int(input())  # nは入力回数
num_list = [int(input()) for _ in range(n)]


# 【n行】n文字
# 3
# aaa b cc
# d ee fff
# gg hhh i

n = int(input())  # nは入力回数
str_list = []
for i in range(n):
    str_list.append(list(input().split()))
print(str_list)

# 【n行】n数字
# 3
# 2 1 3
# 3 1 2 3
# 2 3 2

n = int(input())  # nは入力回数
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))
print(num_list)

##### END #####


# 整数を受け取る場合
N = int(input())

# 小数を受け取る場合
F = float(input())

# リストを逆順にする場合
print(list(reversed(a)))

# 途中終了する場合
sys.exit()

# 配列を特定文字列で区切る場合
x = [1, 2, 3, 4, 5]
for i in x:
    print(i, end=" ")

# copy.deepcopy
B = copy.deepcopy(A)

# slice start <= x < stopの範囲が選択される
l = [0, 10, 20, 30, 40, 50, 60]
print(l[2:5])
# [20, 30, 40]

# 迷路のTOTAL経路数
# https://leetcode.com/problems/unique-paths/submissions/905907730/
