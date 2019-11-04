import sys

av = sys.argv[1:]

if len(av) < 1:
    print("InputError: no arguments provided")
    sys.exit()

if len(av) > 2:
    print("InputError: too many arguments")
    print("Usage: python operations.py")
    print("Example:")
    print("\tpython operations.py 10 3")
    sys.exit()

for i in av:
    if not i.isdigit():
        print("InputError: only numbers")
        print("Usage: python operations.py")
        print("Example:")
        print("\tpython operations.py 10 3")
        sys.exit()

num1 = int(av[0])
num2 = int(av[1])

print("Sum:\t\t", num1 + num2)
print("Difference:\t", num1 - num2)
print("Product:\t", num1 * num2)

if num2:
    print("Quotient:\t", num1 / num2)
    print("Remainder:\t", num1 % num2)
else:
    print("Quotient:\t ERROR (div by zero)")
    print("Remainder:\t ERROR (modulo by zero)")
