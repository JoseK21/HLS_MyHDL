import matplotlib
import matplotlib.pyplot as plt


def simulator(arraySelectedSignals, listValues, lastEdgeValue):
    fig = plt.figure(figsize=[15, 8])
    ax = fig.add_subplot()  # 111

    heigth = 0.5
    middleHeigth = heigth / 2

    ax.set_title('HLS Simulation')
    ax.set_ylabel('Signals')
    ax.set_xlabel('Time (ns)')

    x = list(range(0, lastEdgeValue + 20, 10))

    y = [""] + arraySelectedSignals
    y = y + [""]

    values = range(len(x))
    valuesY = range(len(y))

    counter = 1
    for selected_signal in arraySelectedSignals:
        rect1 = matplotlib.patches.Rectangle((0, counter - middleHeigth), 50, heigth, color='green', joinstyle='miter')

        if(listValues.get(selected_signal) != None):
            for binaryValue in listValues.get(selected_signal):
                xEdge, bValue = binaryValue.split('-')
                plt.text(int(xEdge) // 10, counter - 0.05, bValue)
         
        ax.add_patch(rect1)
        counter += 1

    plt.grid(axis='x')
    plt.xticks(values, x)
    plt.yticks(valuesY, y)


    plt.show()
