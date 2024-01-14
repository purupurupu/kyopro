def digit_sum(n):
    # nを10進法で表したときの各桁の和を計算する関数
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def count_good_integers(N):
    count = 0
    for i in range(1, N+1):
        if i % digit_sum(i) == 0:
            count += 1
    return count

N = int(input())
result = count_good_integers(N)
print(result)
