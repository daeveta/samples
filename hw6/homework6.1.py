b = b"r\xc3\xa9sum\xc3\xa9"
s = b.decode('utf-8')
print(s)
a = s.encode('Latin1')
print(a)
c = a.decode('latin1')
print(c)