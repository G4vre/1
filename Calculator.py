a = float(input("Введите число: "))
b = float(input("Введите число: "))
while True:
    action = input("Введите действие: (+, -, /, *) ")
    result = 0
    if action == "+":
        result =(a+b)
    elif action == "-":
        result =(a-b)
    elif action == "/":
        result =(a/b)
    elif action == "*":
        result =(a*b)
    else:
        print("Вы ввели неверное действие")
        continue


    print(result)
    break

