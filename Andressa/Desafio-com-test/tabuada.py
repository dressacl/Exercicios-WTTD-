num = int(input("Digite o número para calcular:"))

for numero in range(1, 11):
    result = numero * num

    print(num, 'X', numero, '=', result)

assert num * 1 == num
assert numero * num == result
assert num > 0

