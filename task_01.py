# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

UsNumber = int(input('Введите число от 1 до 7: '))

if UsNumber >= 1 and UsNumber <= 5:
    print('Данный день недели ', UsNumber, 'не является выходным')
elif UsNumber>5 and UsNumber<=7:
    print('Данный день недели ', UsNumber, ' является выходным')
else:
    print('Введено неверное число')