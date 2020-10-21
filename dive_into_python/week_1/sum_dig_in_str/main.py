import sys

digit_string = sys.argv[1]
sum_d = 0

for ch in digit_string:
    sum_d += int(ch)

print(sum_d)
