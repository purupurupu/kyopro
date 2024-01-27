S = input()
res =  "Yes" if S[0].isupper() and (len(S) == 1 or S[1:].islower()) else "No"

print(res)