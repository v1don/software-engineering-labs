import string
n=int(input())
m=int(input())

s=''
for i in range(m):
    s=s+'#'

print('ПРЯМОУГОЛЬНИК {}X{}:'.format(n, m))
for i in range(n):
    print(s)

s=''
print('ПРАВЫЙ ТРЕУГОЛЬНИК:')
for i in range(n):
    s=s+'#'
    print(s)

print('РАМКА {}X{}:'.format(n, m))
s=''
for i in range(m):
    s=s+'#'

st=s
print(st)
s='#'
for i in range(m-2):
    s+=' '
s+='#'
for i in range(n-2):
    print(s)
print(st)