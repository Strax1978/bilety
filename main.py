price = 0
ticket = int(input('Количество билетов   '))
for i in range(0, ticket):
    age = int(input(f'Возраст участника №{i + 1}:\n'))
    if age > 100 or age <= 0:
        print("Не может быть столько лет, начните заново")
        break
    if age < 18:
        print('Билет бесплатный')
    elif 25 > age >= 18:
        price += 990
        print('Стоимость билета: 990')
    else:
        price += 1390
        print('Стоимость билета: 1390')
if 3 < ticket >= 4:
    print('Общая сумма за',ticket,"билета со скидкой =" , price * 0.9)
elif ticket >= 5:
    print('Общая сумма за',ticket,"билетов со скидкой =" , price * 0.9)
else:
    print('Общая сумма за',ticket,"билета =", price)