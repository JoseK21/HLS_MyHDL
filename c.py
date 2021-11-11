import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=[15, 8])
ax = fig.add_subplot()  # 111

heigth = 0.5
middleHeigth = heigth / 2



ax.set_title('HLS Simulation')

ax.set_ylabel('Signals')
ax.set_xlabel('Time (ns)')


x= list(range(0, 200 + 1, 10))

y=["", "A" ,"B", "C", "D", "E", ]

values = range(len(x))
valuesY = range(len(y))



plt.grid(axis='x')

# plt.xlim(0, 10, 100, 200)
# plt.ylim([0, 5])

plt.xticks(values,x)
plt.yticks(valuesY, y)


rect1 = matplotlib.patches.Rectangle(
    (0, 1 - middleHeigth), 10, heigth, color='green', joinstyle='miter')

rect2 = matplotlib.patches.Rectangle(
    (0, 4 - middleHeigth), 30, heigth, color='pink', joinstyle='round')

rect3 = matplotlib.patches.Rectangle(
    (0, 3 - middleHeigth), 40, heigth, color='yellow', joinstyle='bevel')

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)

# plt.annotate('0110', xy=(10, 0), xytext=(200, 100 + middleHeigth) )


plt.text(1,1,'011001')

plt.annotate('1010', xy=(1,1), xytext=(2,2), arrowprops=dict(facecolor='black', arrowstyle="<->"))



# v = np.arange(min(0), max(200), 10)

# print(v)

# plt.xticks(v)

plt.show()
