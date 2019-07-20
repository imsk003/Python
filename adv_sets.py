s = set()

s.add(1)
s.add(2)

print(s)

s.clear()

print(s)

s = {1,2,3}
sc = s.copy()

print(sc)
print(s)

print(s.difference(sc))

s.discard(2)
print(s)