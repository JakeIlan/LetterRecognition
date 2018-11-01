import random

# Буквы (Обучающая выборка)
litA = list('111101111101101')
litB = list('111100111101111')
litV = list('110101110101110')
litG = list('111100100100100')
litE = list('111100111100111')
litK = list('101101110101101')
litL = list('010101101101101')
litN = list('101101111101101')
litO = list('111101101101111')
litP = list('111101101101101')

# Список всех вышеуказанных букв (А, Б, В, Г, Е, К, Л, Н, О, П)
lits = [litA, litB, litV, litG, litE, litK, litL, litN, litO, litP]

# Виды буквы А (Тестовая выборка)
litA1 = list('010101111101101')
litA2 = list('011101111101001')
litA3 = list('010101111101000')
litA4 = list('010101111101100')
litA5 = list('110101111101001')
litA6 = list('010101111100101')

# Инициализация весов сети
weights = []
for i in range(15):
    weights.append(0)

# Порог функции активации
bias = 7


# Является ли данное число 5
def proceed(number):
    # Рассчитываем взвешенную сумму
    net = 0
    for i in range(15):
        net += int(number[i]) * weights[i]
    # Превышен ли порог? (Да - сеть думает, что это 5. Нет - сеть думает, что это другая цифра)
    return net >= bias


# Уменьшение значений весов, если сеть ошиблась и выдала 1
def decrease(number):
    for i in range(15):
        # Возбужденный ли вход
        if int(number[i]) == 1:
            # Уменьшаем связанный с ним вес на единицу
            weights[i] -= 1


# Увеличение значений весов, если сеть ошиблась и выдала 0
def increase(number):
    for i in range(15):
        # Возбужденный ли вход
        if int(number[i]) == 1:
            # Увеличиваем связанный с ним вес на единицу
            weights[i] += 1


# Тренировка сети
for i in range(20000):
    # Генерируем случайное число от 0 до 9
    option = random.randint(0, 9)


    # Если получилось НЕ число 5
    if option != 0:
        # Если сеть выдала True/Да/1, то наказываем ее
        if proceed(lits[option]):
            decrease(lits[option])
        # Если получилось число 5
    else:
        # Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно
        if not proceed(litA):
            increase(litA)

# Вывод значений весов
print(weights)

# Прогон по обучающей выборке
print("Б это А? ", proceed(litB))
print("В это А? ", proceed(litV))
print("Г это А? ", proceed(litG))
print("Е это А? ", proceed(litE))
print("К это А? ", proceed(litK))
print("Л это А? ", proceed(litL))
print("Н это А? ", proceed(litN))
print("О это А? ", proceed(litO))
print("П это А? ", proceed(litP), '\n')

# Прогон по тестовой выборке
print("Узнал А? ", proceed(litA))
print("Узнал А - 1? ", proceed(litA1))
print("Узнал А - 2? ", proceed(litA2))
print("Узнал А - 3? ", proceed(litA3))
print("Узнал А - 4? ", proceed(litA4))
print("Узнал А - 5? ", proceed(litA5))
print("Узнал А - 6? ", proceed(litA6))