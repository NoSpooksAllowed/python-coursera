import sys

n = int(sys.argv[1])

for i in range(0, n):
    for j in range(i, n - 1):
        print(" ", end="")

    for x in range(0, i + 1):
        print("#", end="")

    print()
