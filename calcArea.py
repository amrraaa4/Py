#This program will calculate the area of multiple geometric shapes,
#such as the area of a circle, cube, cylinder and a sphere.

import math

pi = math.pi

def circle(radius):
    return pi*(pow(radius, 2))
def cube(side):
    return 6*side*side
def cylinder(radius, height):
    return 2*pi*radius + 2*pi*height

def sphere(radius):
    return 2*pi*(radius**2)

print("Select operation.")

print("1.Area of a circle")

print("2.Area of a cube")

print("3.Area of a cylinder")

print("4.Area of a sphere")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):

        if choice == "1": #pi*(radius**2)
            radius = input("Enter radius of the shape: ")
            print("The area of the circle = Pi*(radius**2).")
            print("Then the area of this circle = ", circle(radius))

        elif choice == "2": #6*side*side
            side = input("Enter side of the cube: ")
            print("The area of a cube = 6*side*side.")
            print("Then the area of this cube = ", cube(side))

        elif choice == "3": #2*pi*radius + 2*pi*height
            radius = input("Enter radius of the shape: ")
            height = input("Enter height of the shape: ")
            print("The area of a cylinder = 2*pi*radius + 2*pi*height.")
            print("Then the area of this cylinder = ", cylinder(radius, height))

        elif choice == "4": #2*pi*(radius**2)
            radius = input("Enter radius of the shape: ")
            print("The area of a sphere = 2*pi*(radius**2).")
            print("Then the area of this sphere = ", sphere(radius))

        next_calc = input("Wanna do another calculation? (yes/no): ")
        if next_calc == "no":
            print("Hope you like this program!")
            break

    else:
        print("Invalid Input")
