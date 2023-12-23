N = int(input())

def func(n):
    repunits = [int("1" * i) for i in range(1, 15)] 
    sums = set()

    for i in repunits:
        for j in repunits:
            for k in repunits:
                sums.add(i + j + k)

    sorted_sums = sorted(list(sums))
    return sorted_sums[n - 1]

res =  func(N)

print(res)