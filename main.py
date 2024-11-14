def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        result = gcd(num1, num2)
        print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}.")

    except ValueError:
        print("Пожалуйста, введите корректные целые числа.")


if __name__ == "__main__":
    main()