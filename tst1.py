num = int(input())
num1 = num // 100
num2 = (num % 100) // 10
num3 = (num % 100) % 10
summa = num1 + num2 + num3
multiply = num1 * num2 * num3
print('Сумма цифр =', summa)
print('Произведение цифр =', multiply)