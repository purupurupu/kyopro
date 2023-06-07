from heapq import heappush, heappop


def solve(N, K, A):
    min_prices = set()
    heap = []

    for price in A:
        heappush(heap, price)

    while K > 0:
        current_price = heappop(heap)
        if current_price not in min_prices:
            min_prices.add(current_price)
            K -= 1

        for price in A:
            new_price = current_price + price
            if new_price not in min_prices:
                heappush(heap, new_price)

    return current_price


# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 出力
answer = solve(N, K, A)
print(answer)
