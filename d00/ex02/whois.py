import sys

av = sys.argv[1:]

if len(av) != 1:
    print("ERROR")
    sys.exit(0)

if not av[0].isdigit():
    print("ERROR")
    sys.exit(0)

num = int(av[0])

if num:
    if not (num % 2):
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    print("I'm Zero.")
