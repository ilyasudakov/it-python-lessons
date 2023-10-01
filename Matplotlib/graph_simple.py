import matplotlib.pyplot as plt

x = [i / 10 for i in range(-50, 51)]

y = [i ** 2 for i in x]

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title = 'График функции y = x^2'

plt.show()