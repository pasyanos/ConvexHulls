import argparse
import numpy as np
from utils import calculateTurnDeterminant
from utils import readPoints
from utils import displayPoints
from utils import writeSolution


# generate a convex hull using a brute force approach
def bruteForceHull(n, xPts, yPts):
    # step 1: initialize an empty solution set
    hullEdges = []

    # Step 2: iterate through all ordered pairs of points in the set P x P where p != q
    # O(n^3) time due to the triple nested loop
    for i in range(n):
        for j in range(n):
            if i != j:
                p = (xPts[i], yPts[i])
                q = (xPts[j], yPts[j])

                # iterate through all other points to determine if the line pq is on the convex hull
                valid = True
                for k in range(n):
                    if k != i and k != j:
                        r = (xPts[k], yPts[k])

                        # use the determinant to determine if the turn is a left turn
                        # if the turn is left, the edge pq is not on the convex hull
                        if calculateTurnDeterminant(p, q, r) >= 0:
                            valid = False
                            break

                # if the edge pq is on the convex hull, add it as a pair to the solution
                if valid:
                    hullEdges.append((p, q))

    # Unlike Graham Scan, the brute force method finds edges, not points,
    # so we have to generate the points from the edges
    ret = []
    for edge in hullEdges:
        p, q = edge
        if p not in ret:
            ret.append(p)
        if q not in ret:
            ret.append(q)

    # the points are not guaranteed to be in our desired counterclockwise order, so sort them
    # I found the solution for sorting in counterclockwise order from
    # https://pavcreations.com/clockwise-and-counterclockwise-sorting-of-coordinates/
    coords = np.array(ret)
    cx, cy = coords.mean(axis=0)
    x, y = coords.T
    angles = np.arctan2(x-cx, y-cy)
    indices = np.argsort(-angles)
    ret = coords[indices]

    return ret, hullEdges


# main entry point for brute-force convex hull generation
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
    solution, edges = bruteForceHull(numPoints, xs, ys)

    # write the solution to the output file
    writeSolution(args.output, solution)

    if args.display:
        displayPoints(numPoints, xs, ys, solution, edges, "Brute Force")
