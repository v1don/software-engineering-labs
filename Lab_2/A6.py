t=int(input())

x=24*60*60
t=t%x

s=t%60
t=t//60

m=t%60
t=t//60

h=t

print('{}:{:02}:{:02}'.format(h,m,s))

