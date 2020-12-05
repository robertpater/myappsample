import pylab as p
x = range(-5, 6)
y = []

for i in x:
    y.append(2 * i + 1)

# print(y)
p.plot(x, y)
p.title('Wykres funkcji 2x+1')
p.grid(True)
p.show()
