import string

s=input()

f=1
if len(s)!=8:
    print("Длина пароля не равна 8")
    f=0

s2=s.lower()
if s==s2:
    print("В пароле отсутствуют заглавные буквы")
    f=0
s2=s.upper()
if s==s2:
    print("В пароле отсутствуют строчные буквы")
    f=0

if any(symbol.isdigit() for symbol in s):
    s=s
else:
    print("В пароле отсутствуют цифры")
    f=0

s2=string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'

if all(symbol in s2 for symbol in s):
    s=s
else:
    print("В пароле используются непредусмотренные символы")
    f=0;

s2="*-#"
if any(symbol in s for symbol in s2):
    s=s
else:
    print("В пароле отсутствуют специальные символы")
    f=0;

if f==1:
    print("Надежный пароль")