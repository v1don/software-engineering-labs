x=float(input())
y=float(input())
x2=float(input())
y2=float(input())

if x > 0 and y > 0:
    s1 = "I"
if x2 > 0 and y2 > 0:
    s2 = "I"


if x < 0 and y > 0:
    s1 = "II"
if x2 < 0 and y2 > 0:
    s2 = "II"


if x < 0 and y < 0:
    s1 = "III"
if x2 < 0 and y2 < 0:
    s2 = "III"


if x > 0 and y < 0:
    s1 = "IV"
if x2 > 0 and y2 < 0:
    s2 = "IV"

if s1==s2:
    print('YES, {}'.format(s1))
else:
    print('NO')