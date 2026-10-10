x=int(input())
y=int(input())

r=y-x if y>x else y-x+10000
r2=r
pay=0

if r<=300:
    pay+=21
    r=0
else:
    pay+=21
    r-=300

if r<=300:
    pay+=r*0.06
    r=0
else:
    pay += 300 * 0.06
    r-=300
if r<=200:
    pay+=r*0.04
    r=0
if r>200:
    pay+=200*0.04
    r-=200
pay+=r*0.025
sr=pay/r2

headers = ["Предыдущее", "Текущее", "Использовано", "К оплате", "Ср. цена m^3"]
values = [
    str(x),
    str(y),
    str(r2),
    f"{pay:.2f}",
    f"{sr:.2f}"
    ]
print("  ".join(f"{h:<14}" for h in headers))
print("  ".join(f"{v:<14}" for v in values))