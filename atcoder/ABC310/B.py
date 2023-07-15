def resolve():
    N, M = map(int, input().split())
    items = []
    for _ in range(N):
        data = list(map(int, input().split()))
        price = data[0]
        features = set(data[2:])
        items.append((price, features))

    for j in range(N):
        for i in range(N):
            if i != j and items[i][0] >= items[j][0] and items[i][1].issubset(items[j][1]) and (items[i][0] > items[j][0] or items[j][1] - items[i][1]):
                return 'Yes'
    return 'No'


print(resolve())
