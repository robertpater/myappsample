# trzeba zainstalowac matplotlib
# https://matplotlib.org/users/installing.html
# easy
# python -m pip install -U pip
# python -m pip install -U matplotlib

import matplotlib.pyplot as plt


def next_vertex(x, y):
    h = (x**2 + y**2)**0.5
    return (x - y / h, y + x / h)


plt.axes().set_aspect(1)
plt.axis('off')

# base of the first triangle
plt.plot([0, 1], [0, 0])

N = 17
x_old, y_old = 1, 0
for n in range(1, N):
    x_new, y_new = next_vertex(x_old, y_old)
    # draw short side
    plt.plot([x_old, x_new], [y_old, y_new])
    # draw hypotenuse
    plt.plot([0, x_new], [0, y_new])
    x_old, y_old = x_new, y_new
# w katalogu z ktorego uruchamiasz zrobic nowy plik PNG z wynikiem
plt.show()
