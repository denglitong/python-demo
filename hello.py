#!/usr/bin/env python3

# print("hello, world!")

a = 100

if a >= 0:
    print(a)
else:
    print(-a)

a = "string"

print(a)

a = 1
a = 100
a = -8080
a = 0xff00

a = 10_0_00_000
print(a)

a = 0xa1b2_c3d4_5
print(a)

a = 1.23
a = 3.14
a = -9.01
print(a)

a = 1.23e9
print(a)

a = 'I\'m "OK"'
print(a)

raw = r'""\n\t'
print(raw)

complexRaw = r'''--begin
    hello from the other side,
i must have called you thousand times\n
---end
'''

print(complexRaw)

b = False
b = True
print(b)

print(b and False)
print(False or False)
print(not False)

nil = None
print(nil)

PI = 3.14159
print(PI)

divide = 10 / 3
print(divide)  # 3.333333

floorDivide = 10 // 3
print(floorDivide)  # 3

print(10 % 3)  # 1

print("包含中文的str")

print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')  # 中文

strBytes = b'ABC'
print(strBytes)

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
