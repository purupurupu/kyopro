import sys
s = input()

stack = []  # スタック
for c in s:
    if c == '(':
        # '(' がある場合はスタックに push
        stack.append(c)
    elif c == ')':
        # ')' がある場合はスタックから pop
        if not stack:
            # スタックが空の場合は、操作を完了できない
            print("False")
            sys.exit()
        stack.pop()
    else:
        # スタックが空でない場合は、操作を完了できない
        if stack:
            print("False")
            sys.exit()
print("True")
