WATER_ML_PER_KG = 30 
ML_PER_LITER = 1000 

user_name = input('Привет, как тебя зовут? ')
print(f'Приятно познакомиться, {user_name}!')
user_age = int(input('Сколько тебе лет? '))
user_weight = float(input('Введите ваш вес (в кг): ').replace(',', '.'))
# При вводе через запятую была ошибка.
# Изучил её и нашёл решение replace(',', '.')
user_height = float(input('Введите ваш рост (в метрах): ').replace(',', '.'))

bmi = user_weight / (user_height ** 2)
water_ml = user_weight * WATER_ML_PER_KG
water_l = water_ml / ML_PER_LITER

print()
print(f'Отчет для пользователя: {user_name} ({user_age} л.)')
print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {round(water_l, 1)} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
