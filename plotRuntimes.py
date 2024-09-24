import matplotlib
import matplotlib.pyplot
import numpy as np

inputSize = ["10", "100", "1000", "10000", "100000", "500000", "1000000"]

bruteForceTimes = [0.003, 0.322, 41.413]

grahamScanTimes = [0.001, 0.003, 0.247, 0.254, 0.327, 11.682, 23.978]

if __name__ == "__main__":
    # make a bar graph of the runtimes
    x = np.arange(len(inputSize))
    width = 0.5

    fig, ax = matplotlib.pyplot.subplots(layout="constrained")

    for i in range(len(inputSize)):
        offset = width * i
        rect1, rect2 = None, None
        if i < len(bruteForceTimes):
            rect1 = ax.bar(i + offset, bruteForceTimes[i], width, label='Brute Force', color='b')
        if i < len(grahamScanTimes):
            rect2 = ax.bar(i + offset + width, grahamScanTimes[i], width, label='Graham Scan', color='r')

        if rect1 is not None:
            ax.bar_label(rect1, padding=3)
        if rect2 is not None:
            ax.bar_label(rect2, padding=3)

    matplotlib.pyplot.yscale('log')

    # labels
    ax.set_ylabel('Time (s)')
    ax.set_title("Convex Hull Runtimes by Input Size")
    # set x ticks to the input sizes
    ax.set_xticks(x*width*3 + width/2, inputSize)
    ax.set_xlabel('Input Size')
    ax.set_ylim(0.001, 300)

    matplotlib.pyplot.show()
