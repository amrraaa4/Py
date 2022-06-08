import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def sqr(n):
    return pow(n, 2)

def pw3(n):
    return pow(n, 3)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Power of 3")

while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        next_calc = input("Wanna do another calculation? (yes/no): ")
        if next_calc == "no":
            print("Hope you like this program!")
            break

    elif choice in ("5", "6"):
        n = float(input("Enter number: "))
        if choice == '5':
            print(n, "^ 2 = ", sqr(n))
        elif choice == '6':
            print(n, "^ 3 = ", pw3(n))
        
        next_calc = input("Wanna do another calculation? (yes/no): ")
        if next_calc == "no":
            print("Hope you like this program!")
            break
    else:
        print("Tnvalid Input")
