x=int(input())
y=int(input())
x2=int(input())
y2=int(input())

col1='White' if x%2==y%2 else 'Black'
col2='White' if x2%2==y2%2 else 'Black'

if col1==col2:
    print('YES')
    print(col1)
else:
    print('NO')