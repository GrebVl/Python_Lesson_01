# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

count = 0
print('X', 'Y', 'Z')
for i in range(0, 8):
    num = bin(i)
    num = num.replace('b', '0')
    X = int(num[-3])
    Y = int(num[-2])
    Z = int(num[-1])
    ferstStatement = not(X or Y or Z)
    secondStatement=(not X) and (not Y) and (not Z)
    if ferstStatement == secondStatement:
        count += 1
        print(X, Y, Z, ferstStatement, secondStatement, count)


if count == 8:
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z утверждение истеннно")
else:
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z утверждение ложно")


