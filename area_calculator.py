from math import pi

print("==================")
print("Area Calculator 📐")
print("==================")

def square(x):
    area = x ** 2
    print(f"\nThe area is {area}.\n")

def rectangle(x, y):
    area = x * y
    print(f"\nThe area is {area}.\n")

def triangle(x, h):
    area = (x * h)/2
    print(f"\nThe area is {area}.\n")

def circle(r):
    area = pi * (r**2)
    print(f"\nThe area is {area}.\n")

cont = True
while cont==True:
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Exit\n")

    shape = int(input("Choose a shape: "))
    print("")
    if shape == 1:
        h = int(input("Height: "))
        x = int(input("Base: "))
        triangle(x, h)
    elif shape == 2:
        x = int(input("Length: "))
        y = int(input("Width: "))
        rectangle(x, y)
    elif shape == 3:
        x = int(input("Side: "))
        square(x)
    elif shape == 4:
        r = int(input("Radius: "))
        circle(r)
    elif shape == 5:
        cont = False
    else:
        print("Wrong option!")