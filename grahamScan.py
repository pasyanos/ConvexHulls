import argparse
from utils import readPoints
from utils import displayPoints
from utils import writeSolution
from collections import deque
from utils import calculateTurnDeterminant
import numpy as np


# calculate the polar angle between a point and the horizontal axis of the given pivot point
def polarAngle(point, pivotPt):
    return np.angle(point[0] - pivotPt[0] + 1j * (point[1] - pivotPt[1]))


def sortByAngle(pivotPt, points):
    points.sort(key=lambda x: polarAngle(x, pivotPt))
    return points


def grahamScan(n, xPts, yPts):
    # step 1: find the bottom most point in O(n) time
    bottomIndex = 0
    for i in range(1, n):
        if yPts[i] < yPts[bottomIndex]:
            bottomIndex = i
        # use leftmost x value to break ties
        elif yPts[i] == yPts[bottomIndex] and xPts[i] < xPts[bottomIndex]:
            bottomIndex = i

    bottomPoint = (xPts[bottomIndex], yPts[bottomIndex])

    # sort the points by the angle they make with the bottom point
    points = []
    for i in range(n):
        if i != bottomIndex:
            points.append((xPts[i], yPts[i]))

    # O(n log n) time to sort points
    points = sortByAngle(bottomPoint, points)

    # make a stack and initialize it with the bottom point
    stack = deque()
    stack.append((xPts[bottomIndex], yPts[bottomIndex]))

    # # debug: add all sorted points to the stack
    # # and add an edge between the bottom point and the first point
    # for point in points:
    #     stack.append(point)
    #     hullEdges.append((bottomPoint, point))

    for i in range(n - 1):
        while len(stack) > 1 and calculateTurnDeterminant(stack[-2], stack[-1], points[i]) < 0:
            stack.pop()
        stack.append(points[i])


    return stack


# main entry point for graham scan convex hull generation
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

    # read in the points from the input file
    fileName = args.input
    numPoints, xs, ys = readPoints(fileName)

    # calculate brute-force convex hull
    solution = grahamScan(numPoints, xs, ys)

    # write the solution to the output file
    writeSolution(args.output, solution)

    if args.display:
        # make edges from the solution points
        edges = [(solution[i], solution[i + 1]) for i in range(len(solution) - 1)]
        # add the last edge from the last point to the first point
        edges.append((solution[-1], solution[0]))
        displayPoints(xs, ys, solution, edges)
