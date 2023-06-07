import sys
import re

S = input()


str_length = len(S)

if str_length < 8:
    print("No")
    sys.exit()

uppercase_characters = re.findall(r"[A-Z]", S)


if len(uppercase_characters) > 2:
    print("No")
    sys.exit()


if not S[0].isupper:
    print("No")
    sys.exit()

if not S[str_length-1].isupper:
    print("No")
    sys.exit()

check_num = int(S[1:len(S)-1])

if len(str(check_num)) < 6:
    print("No")
    sys.exit()

if S[0].isupper() and 100000 <= int(S[1:7]) <= 999999 and S[7].isupper() and S[-1].isupper():
    print("Yes")
else:
    print("No")
