import argparse
from utils import calculateTurnDeterminant
from utils import readPoints
from utils import displayPoints
from utils import writeSolution


# Jarvis March algorithm
def jarvisMarch(n, xPts, yPts):
    ret = []

    # step 1: find the bottom most point in O(n) time
    bottomIndex = 0
    for i in range(1, n):
        if yPts[i] < yPts[bottomIndex]:
            bottomIndex = i
        # use leftmost x value to break ties
        elif yPts[i] == yPts[bottomIndex] and xPts[i] < xPts[bottomIndex]:
            bottomIndex = i

    #debug, todo: remove
    numIters = 0


if __name__ == '__main__':
    # take in arguments
    parser = argparse.ArgumentParser()

    # require an input file to read from
    parser.add_argument('input', help='Input file to read from', type=str)

    # require an output file to read to
    parser.add_argument('output', help='Output file to write to', type=str)

    # add an optional bool argument to display the points
    parser.add_argument('--display', help='Display the points in a scatter plot', type=bool,
                        default=False)

    args = parser.parse_args()
    fileName = args.input

    numPoints, xs, ys = readPoints(fileName)

    solution = jarvisMarch(numPoints, xs, ys)

    writeSolution(args.output, solution)

    if args.display:
        # make edges from the solution points
        solutionEdges = [(solution[i], solution[i + 1]) for i in range(len(solution) - 1)]
        displayPoints(xs, ys, solution, solutionEdges)
