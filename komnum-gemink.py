###
# Problem: 
#   Implementasikan algoritma metode Bolzano menjadi sebuah program komputer yang dapat
#   menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya.
#
# Muhammad Razan Athallah - 5025211008
# Alexander Weynard Samsico - 5025211014
# Revanantyo Dwigantara - 5025211113
# Apta Rasendriya Wijaya - 5025211139
# Akhmad Mustofa Solikin - 5025211230
###

from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

fx = []
x = []
table = []
rows = 0

def func(x):
    return pow(x, 3) - 4 * pow(x, 2) - 7 * x + 10

def root(xl, xu):
    xr = (xl + xu) / 2
    fl = func(xl)
    fr = func(xr)

    global rows
    if (rows < maxit):
        x.append(xr)
        fx.append(fr)
        rows = rows + 1
        table.append([rows, xl, xu, xr, fl, fr, fl*fr])
        # table.append([rows, "{:.6f}".format(xl), "{:.6f}".format(xu), "{:.6f}".format(xr),
        #             "{:.6f}".format(fl), "{:.6f}".format(fr), "{:.6f}".format(fl*fr)])

    if (fl * fr == 0): print("akar: " + "{:.2f}".format(xr))
    elif (fl * fr < 0): root(xl, xr)
    elif (fl * fr > 0): root(xr, xu)

xl = float(input())
xu = float(input())
maxit = int(input())
root(xl, xu)

print(tabulate(table, headers = ["iterasi", " xl", "xu", "xr", "f(xl)", "f(xr)", "f(xl) * f(xr)"], tablefmt = 'grid'))

model = np.poly1d(np.polyfit(x, fx, 2))
polyline = np.linspace(min(x), max(x), 50)

plt.ylabel('f(x)')
plt.xlabel('x')
plt.scatter(x, fx)
plt.plot(polyline, model(polyline), color='red')
plt.show()
