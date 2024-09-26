import argparse
import numpy as np
from collections import deque
from datetime import datetime
from utils import readPoints
from utils import displayPoints
from utils import writeSolution
from utils import calculateTurnDeterminant
from utils import calculateRuntime


# calculate the polar angle between a point and the horizontal axis of the given pivot point
def polarAngle(point, pivotPt):
    return np.angle(point[0] - pivotPt[0] + 1j * (point[1] - pivotPt[1]))


# sort in place using the polarAngle method
def sortByAngle(pivotPt, points):
    points.sort(key=lambda x: polarAngle(x, pivotPt))
    return points


# generate a convex hull using the Graham Scan algorithm
def grahamScan(n, xPts, yPts):
    # step 1: find the bottom most point
    # O(n) time to find the point
    bottomIndex = 0
    for i in range(1, n):
        if yPts[i] < yPts[bottomIndex]:
            bottomIndex = i
        # use leftmost x value to break ties
        elif yPts[i] == yPts[bottomIndex] and xPts[i] < xPts[bottomIndex]:
            bottomIndex = i

    bottomPoint = (xPts[bottomIndex], yPts[bottomIndex])

    # Step 2a: make a list of the remaining points, excluding the bottom point
    # O(n) time to make the list
    points = []
    for i in range(n):
        if i != bottomIndex:
            points.append((xPts[i], yPts[i]))

    # Step 2b: sort the points by polar angle
    # O(n log n) time to sort points
    points = sortByAngle(bottomPoint, points)

    # Step 3a: make a stack and initialize it with the bottom point
    stack = deque()
    stack.append((xPts[bottomIndex], yPts[bottomIndex]))

    # Step 3b: iterate through the sorted points, adding them to the stack
    # then popping points off the stack when a right turn is made
    # repeat until it is a left turn again
    # O(n) time to iterate through the remaining points
    for i in range(n - 1):
        while len(stack) > 1 and calculateTurnDeterminant(stack[-2], stack[-1], points[i]) < 0:
            stack.pop()
        stack.append(points[i])

    # algorithm is finished; return the final stack
    return stack


# main entry point for graham scan convex hull generation
if __name__ == '__main__':
    # take in arguments
    parser = argparse.ArgumentParser()

    # require an input file to read from
    parser.add_argument('input', help='Input file to read from', type=str)

    # add an optional bool argument to display the points
    parser.add_argument('--display', help='Display the points in a scatter plot', type=bool,
                        default=False)

    # add an optional bool argument to print the runtime to console
    parser.add_argument('--runtime', help='Print the runtime to console', type=bool,
                        default=False)

    args = parser.parse_args()

    startTime = datetime.now()

    # read in the points from the input file
    fileName = args.input
    numPoints, xs, ys = readPoints(fileName)

    # calculate brute-force convex hull
    solution = grahamScan(numPoints, xs, ys)

    outFileName = fileName.split('.')[0] + "_out_graham_scan.txt"
    # write the solution to the output file
    writeSolution(outFileName, solution)

    endTime = datetime.now()

    # perform optional actions if specified by flags
    if args.runtime:
        print("Runtime: ", calculateRuntime(startTime, endTime))

    if args.display:
        displayPoints(numPoints, xs, ys, solution, "Graham Scan")
