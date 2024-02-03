N = int(input())
A = list(map(int, input().split()))

# min_initial + current_passengers を最小化する
min_initial = 0
current_passengers = 0

for change in A:
    current_passengers += change
    # 0以上の乗客数を保つために、最小の初期乗客数を更新する
    if current_passengers < 0:
        min_initial = max(min_initial, -current_passengers)

res = min_initial + current_passengers

print(res)