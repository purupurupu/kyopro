N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

min_dish_price = min(D)
min_total_price_with_discount = Q + min_dish_price

if min_total_price_with_discount < P:
    print(min_total_price_with_discount)
else:
    print(P)
