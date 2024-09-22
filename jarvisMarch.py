import argparse
import numpy as np
from utils import readPoints
from utils import displayPoints
from utils import writeSolution


# given three points p,q,r, determine if the turn is left or collinear, or right
# by calculating the determinant
def calculateTurn(p, q, r):
    # use the determinant of the matrix formed by the three points
    mat = np.array([[1, p[0], p[1]],
                    [1, q[0], q[1]],
                    [1, r[0], r[1]]])

    det = ((mat[1][1] - mat[0][1]) * (mat[2][2] - mat[0][2])
           - (mat[2][1] - mat[0][1]) * (mat[1][2] - mat[0][2]))

    return det


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

    # set up first two points for turn calculation
    indexP = -1
    indexQ = bottomIndex

    # for readability, I'm making a bool to check if we are back at the first point
    backAtStart = False

    # step 2: h iterations to find the points on the convex hull
    # where h is the number of points on the hull
    while not backAtStart:
        # need a special case for p if this is the first iteration
        p = (xPts[indexP], yPts[indexP]) if indexP >= 0 else (xPts[indexQ] - 1, yPts[indexQ])
        q = (xPts[indexQ], yPts[indexQ])

        # add q to the convex hull solution
        ret.append(q)

        # iterate through all other points to determine if the line pq is on the convex hull
        # O(n) time
        for i in range(n):
            r = (xPts[i], yPts[i])
            # if the turn is left, update q to r
            if calculateTurn(p, q, r) >= 0:
                q = r

        # if we are back at the start, break the loop
        if indexQ == bottomIndex:
            backAtStart = True

    return ret


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
