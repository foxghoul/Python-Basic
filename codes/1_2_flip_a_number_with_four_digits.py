# flip a number of four digits
num = int(1234)
n = list(range(len(str(num)) + 1))[:0:-1]
print(n)
num3 = 0
for i in n:
    n0 = num % 10
    num = (num - n0) / 10
    num2 = n0 * 10 ** (i - 1)
    num3 = num3 + num2
print(int(num3))

# print(num)
# n1 = num % 10
# num = (num - n1) / 10
# print(num)
# n2 = num % 10
# num = (num - n2) / 10
# print(num)
# n3 = num % 10
# num = (num - n3) / 10
# print(num)
# num = n0 * 1000 + n1 * 100 + n2 * 10 + n3 * 1
# print(num)

