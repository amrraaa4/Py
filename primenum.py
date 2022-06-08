num = int(input("Enter a number to check if it's a prime number or not: "))

for i in range(2,num):
    if num % i == 0:
        print("This number not a prime number.")
        break
    else:
        print("This number is a prime number.")
        break
