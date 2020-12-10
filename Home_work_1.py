#первая задача
original_pasword = "Misha2110"
paasword = input("Введите пароль: ")
access = False
if paasword == original_pasword:
    access = True
    print("Добро пожаловать в систему!")

while paasword != original_pasword:
    paasword = input("Введите пароль заного: ")
    if paasword == original_pasword:
        break

print("Добро пожаловать в систему")


#вторая задача
user_value = int(input("Введите секунды"))
h = user_value // 3600
m = (user_value - h * 3600) // 60
s = user_value - (h * 3600 + m * 60)
print(f"Время в формате чч:мм:сс  {h}:{m}:{s} ")

#третья задача

user_n = int(input("Введите ваше число: "))
m = user_n + (user_n * 10)

m_2 = user_n * 100 + m

m_3 = user_n + m + m_2

print(f"Ваш ответ равен {user_n} + {m} + {m_2} =  {m_3}")

#4 задача
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break



profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit - costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
    a += 0.1 * a
    result_days += 1
    result_km = a
print(f"Вы достигнете требуемых показателей на {result_days} день" )
