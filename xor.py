x = hex(7)
b = hex(8)

b = b.encode('utf-8')
x = x.encode('utf-8')

print(b ^ x)
