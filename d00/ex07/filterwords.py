import sys
import re


av = sys.argv[1:]

if not av[1].isdigit():
    print("ERROR")
    sys.exit()

if not isinstance(av[0], str):
    print("ERROR")
    sys.exit()

if len(av) != 2:
    print("ERROR")
    sys.exit()

s = re.sub(r"[!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", '', av[0])
s = ' '.join([w for w in s.split() if len(w) > int(av[1])])
s = s.split(' ')

print(s)
