import argparse
from utils import readPoints
from utils import displayPoints


# placeholder for Jarvis March algorithm
def jarvisMarch(n, xPts, yPts):
    return []


if __name__ == '__main__':
    # take in arguments
    parser = argparse.ArgumentParser()

    # require an input file to read from
    parser.add_argument('input', help='Input file to read from', type=str)

    # add an optional bool argument to display the points
    parser.add_argument('--display', help='Display the points in a scatter plot', type=bool,
                        default=False)

    args = parser.parse_args()
    fileName = args.input

    numPoints, xs, ys = readPoints(fileName)

    solution = jarvisMarch(numPoints, xs, ys)

    if args.display:
        displayPoints(xs, ys, solution)
