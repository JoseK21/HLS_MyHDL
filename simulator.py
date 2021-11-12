import matplotlib
import matplotlib.pyplot as plt


def simulator(YY, maxXX):
    fig = plt.figure(figsize=[15, 8])
    ax = fig.add_subplot()  # 111

    heigth = 0.5
    middleHeigth = heigth / 2

    ax.set_title('HLS Simulation')
    ax.set_ylabel('Signals')
    ax.set_xlabel('Time (ns)')

    x = list(range(0, maxXX + 20, 10))

    y = [""] + YY
    y = y + [""]

    values = range(len(x))
    valuesY = range(len(y))

    counter = 1
    for a in YY:
        rect1 = matplotlib.patches.Rectangle((0, counter - middleHeigth), 50, heigth, color='green', joinstyle='miter')

        ax.add_patch(rect1)
        counter += 1

    plt.grid(axis='x')
    plt.xticks(values,x)
    plt.yticks(valuesY, y)
    plt.text(1,1,'011001')
    plt.annotate('1010', xy=(1,1), xytext=(2,2), arrowprops=dict(facecolor='black', arrowstyle="<->"))

    plt.show()
