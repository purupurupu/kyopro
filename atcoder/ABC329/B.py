N = int(input())
A = list(map(int, input().split()))  # n個の数字がリストに格納される

max_number = max(A)
numbers_without_max = [num for num in A if num != max_number]

print(max(numbers_without_max))