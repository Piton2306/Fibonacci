'''Последовательность Фибоначчи'''
a = int(input())
a1 = 0
b1 = 1
num = 0
for _ in range(a):
    num = a1 + b1
    b1 = a1
    a1 = num
    print(num,end=' ')

