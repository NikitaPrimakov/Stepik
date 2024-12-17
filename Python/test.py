intNum = int(input("Введите исходное 3-х значное число: "))
firstNum = intNum // 100 # первая цифра
secondNum = intNum % 10  # вторая цифра
thirdNum = (intNum // 10) % 10 # третья цифры
print(firstNum, secondNum, thirdNum)