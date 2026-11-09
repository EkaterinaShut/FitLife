# Проект FitLife - MVP версия 1.0
print('Привет! Я бот FitLife. Давай познакомимся.')

# 1. Знакомство
user_name = input('Как вас зовут? ').title()
user_age = int(input('Сколько вам лет? '))

# 2. Сбор данных, обработка ввода
while True:
    try:
        user_weight = float(input('Введите свой вес (в кг): '))
        break  # Если число введено верно, выходим из цикла
    except ValueError:
        print('Ошибка: вес должен быть числом (в кг, например 53.4)!'
              'Попробуйте снова.')

while True:
    try:
        user_height = float(input('Введите свой рост '
                                  '(в метрах, например 1.75): '))
        break  # Если число введено верно, выходим из цикла
    except ValueError:
        print('Ошибка: рост должен быть числом (в метрах, например 1.75)!'
              'Попробуйте снова.')

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

WATER_PER_KG = 30
ML_PER_LITER = 1000
# Подсчет воды: вес * 30 мл
water_needed = user_weight * WATER_PER_KG
# Перевод в литры
water_liters = water_needed / ML_PER_LITER

# 4. Вывод красивого результата
print(
    f'Отчёт для пользователя: {user_name} ({user_age} г.)',
    f'Ваш Индекс Массы Тела: {bmi}',
    f'Рекомендуемая норма воды: {water_liters:.2f} л. в день',
    'Расчет окончен. Будьте здоровы!',
    sep='\n',
)
