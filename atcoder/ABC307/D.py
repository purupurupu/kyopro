# def solve(N, S):
#     stack = []
#     for ch in S:
#         if ch == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(ch)
#         elif ch == '(':
#             stack.append(ch)
#         else:
#             if not stack or stack[-1] != '(':
#                 stack.append(ch)
#     return ''.join(stack)


# N = int(input().strip())
# S = input().strip()

# print(solve(N, S))


# def solve(N, S):
#     stack = []
#     open_brackets = []
#     for ch in S:
#         if ch == '(':
#             open_brackets.append(len(stack))
#             stack.append(ch)
#         elif ch == ')':
#             if open_brackets:
#                 i = open_brackets.pop()
#                 stack = stack[:i+1]  # keep the opening bracket
#             stack.append(ch)
#         else:  # alphabet characters
#             stack.append(ch)

#     # Now remove all pairs of brackets from the stack
#     while True:
#         new_stack = []
#         i = 0
#         while i < len(stack):
#             if i+1 < len(stack) and stack[i] == '(' and stack[i+1] == ')':
#                 i += 2
#             else:
#                 new_stack.append(stack[i])
#                 i += 1
#         if len(new_stack) == len(stack):
#             break
#         stack = new_stack

#     return ''.join(stack)


# N = int(input().strip())
# S = input().strip()

# print(solve(N, S))


def solve(N, S):
    stack = []
    open_brackets = []
    for ch in S:
        if ch == '(':
            open_brackets.append(len(stack))
            stack.append(ch)
        elif ch == ')':
            if open_brackets:
                i = open_brackets.pop()
                stack = stack[:i+1]  # keep the opening bracket
            stack.append(ch)
        else:  # alphabet characters
            stack.append(ch)

    # Now remove all pairs of brackets from the stack
    while True:
        i = j = 0
        while i < len(stack):
            if i+1 < len(stack) and stack[i] == '(' and stack[i+1] == ')':
                i += 2
            else:
                stack[j] = stack[i]
                i += 1
                j += 1
        if j == len(stack):
            break
        stack = stack[:j]

    return ''.join(stack)


N = int(input().strip())
S = input().strip()

print(solve(N, S))
