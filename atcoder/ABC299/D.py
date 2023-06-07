from bisect import bisect_right


def primes(n):
    """エラトステネスの篩により、n以下の素数を列挙する関数"""
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i**2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


def solve(n):
    # N以下の素数を列挙する
    primes_list = primes(int(n**(1/3))+1)

    # a^2 ×b×c^2 を表せる数をカウントする
    count = 0
    for i in range(len(primes_list)):
        p1 = primes_list[i]
        if p1**2 > n:
            break
        for j in range(i+1, len(primes_list)):
            p2 = primes_list[j]
            if p1**2 * p2 > n:
                break
            k = bisect_right(primes_list, int(n/(p1**2 * p2)))
            for l in range(k, len(primes_list)):
                p3 = primes_list[l]
                if p1**2 * p2 * p3**2 > n:
                    break
                count += 1
            else:
                continue
            break
    return count


n = int(input())
print(solve(n))
