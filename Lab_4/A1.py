import random
import time

n=int(input("Введите количество примеров:"))
k=0
s_timer=time.time()

for i in range(1, n+1):
    print('Вопрос {}/{}'.format(i, n))
    a=random.randint(2,9)
    b=random.randint(2,9)
    ans1=a*b
    start_t=time.time()
    while True:
        try:
            ans2 = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    t=time.time()-start_t
    if ans1 == ans2:
        print('Верно! (Время: {:.1f})'.format(t))
        k=k+1
    else: print('Неверно! Правильно: {} (Время: {:.1f})'.format(ans1, t))

timer=time.time()-s_timer
print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print('Общее время: {:.1f} секунд'.format(timer))
print('Среднее время на вопрос: {:.1f} сек'.format(timer/n))
print('Правильных ответов: {}/{}'.format(k, n))
print('Процент правильных: {:.1f}%'.format(k*100/n))