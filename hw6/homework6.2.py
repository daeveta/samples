a = 'apple'
b = 'banana'
c = 'coconut'
d = 'avocado'

with open('homework6.2.1.py', 'w') as f:
    f.write(a + '\n')
    f.write(b + '\n')
f.close()
with open('homework6.2.1.py', 'a') as f:
    f.write(c + '\n')
    f.write(d + '\n')
f.close()