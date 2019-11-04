import sys

array = sys.argv[1:]
array = array[len(array)::-1]

for idx, item in enumerate(array):
    array[idx] = item.swapcase()
    array[idx] = array[idx][len(item)::-1]

print(*array)
