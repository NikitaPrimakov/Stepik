#####################################################
## День 5. Решение задач                            #
#####################################################

# Задача 1

#  Площадь треугольнака
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

square  = (1/2) * a * b
print("Площадь прямоугольного треугольника равна:", square)


# Задача 2

# Две старушки идут навстречу друг другу с постоянными скоростями V1 1​  и V2 2​  км/ч. Определите, через какое время (в часах) 
# старушки встретятся, если расстояние между ними равно S км.

# На вход программе подаются три действительных числа S,V1,V2​ каждое на отдельной строке.

S = float(input("Введите расстояние: "))
V_1 = float(input("Скорость первой бабушки: "))
V_2 = float(input("Скорость второй бабушки: "))

t = S / (V_1 + V_2)
print(t)

# Задача 3

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. 
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

num = float(input("Введите число: "))

if num > 0 or num < 0:
    num = 1/(num**1)
    print(num)
else:
    print("Обратного числа не существует")
    
    
# Задача 4

# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, 
# которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

# Для получения градусов по Цельсию из градусов по Фаренгейту используйте следующую формулу:
# t_c = 5/9 * (t_f - 32)

# где t_f – температура в градусах по Фаренгейту.

t_f = float(input("Введите температуру в градусах по Фаренгейту: "))

t_c = (5/9) * (t_f - 32)

print(t_c)

# Задача 5

# На вход программе подаётся число n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в 
# человеческих годах по следующему алгоритму: в течение первых двух лет собачий год равен 10.5 человеческим годам, 
# после этого каждый год собаки равен 4 человеческим годам.

ageOfDog = float(input("Введите возраст собаки: "))

if ageOfDog >= 2:
    ageOfDog_1 = ageOfDog - (ageOfDog - 1)
    ageOfDog_2 = ageOfDog - (ageOfDog - 2)
    ageOFDog_for2year = ageOfDog_2 * 10.5 # за первые два года
    ageOFDog_other = (ageOfDog - 2) * 4   # стальные годы
    ageOfDog_final = ageOFDog_for2year + ageOFDog_other
    print(ageOfDog_final)
elif 1 <= ageOfDog < 2:
    ageOfDog_1 = ageOfDog - (ageOfDog - 1)
    ageOFDog_for1year = ageOfDog_1 * 10.5
    print(ageOFDog_for1year)
    

# Альтернатива

age = int(input())
if 0 < age <= 2:
    print(age * 10.5)
else:
    print(2 * 10.5 + (age - 2) * 4)
    

# Задача 6

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

num = float(input("Введите число: "))

print(int(num * 10 % 10))


# Задача 7

# Дано положительное действительное число. Выведите его дробную часть.

a = float(input("Введите число: "))

print(a - int(a))

# задача 8

# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел и выводит текст в следующем формате:

# Наименьшее число = <наименьшее число>
# Наибольшее число = <наибольшее число>

firstNum, secondNum, thirdNum, fourthNum, fifthNum = int(input()), int(input()), int(input()), int(input()), int(input())
print("Наименьшее число =", min(firstNum, secondNum, thirdNum, fourthNum, fifthNum))
print("Наибольшее число =", max(firstNum, secondNum, thirdNum, fourthNum, fifthNum))

# Задача 9

# Напишите программу, которая упорядочивает три числа от большего к меньшему.
firstNum, secondNum, thirdNum = int(input()), int(input()), int(input())

if min(firstNum, secondNum, thirdNum) == firstNum and max(firstNum, secondNum, thirdNum) == thirdNum:
    print(thirdNum, secondNum, firstNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == firstNum and max(firstNum, secondNum, thirdNum) == secondNum:
    print(secondNum, thirdNum, firstNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == thirdNum and max(firstNum, secondNum, thirdNum) == secondNum:
    print(secondNum, firstNum, thirdNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == secondNum and max(firstNum, secondNum, thirdNum) == firstNum:
    print(firstNum, thirdNum, secondNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == thirdNum and max(firstNum, secondNum, thirdNum) == firstNum:
    print(firstNum, secondNum, thirdNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == secondNum and max(firstNum, secondNum, thirdNum) == thirdNum:
    print(thirdNum, firstNum, secondNum, sep='\n')
    
# Альтернатива

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))


# Задача 10

# Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре. 
# Напишите программу, которая определяет, интересное число или нет. Если число интересное, 
# следует вывести текст «Число интересное» (без кавычек), иначе – «Число неинтересное» (без кавычек).

intNum = int(input("Введите исходное 3-х значное число: "))
firstNum = intNum // 100 # первая цифра
secondNum = intNum % 10  # вторая цифра
thirdNum = (intNum // 10) % 10 # третья цифры
print(firstNum, secondNum, thirdNum)



