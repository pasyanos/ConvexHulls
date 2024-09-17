import argparse
from utils import readPoints
from utils import displayPoints


def bruteForceHull(n, xPts, yPts):
    ret = []

    # nested loop to compare all points
    # O(n^3) time complexity - 3 nested loops going through all points
    for i in range(n):
        for j in range(n):
            # don't compare the same point
            if i == j:
                continue

            p = (xPts[i], yPts[i])
            q = (xPts[j], yPts[j])

            # all comparisons valid at start
            valid = True

            # loop through all other points that are not p and q
            for k in range(n):
                if k == i or k == j:
                    continue

                # if the point is on the right side of the line, it is not valid
                if (xPts[k] - p[0]) * (q[1] - p[1]) - (yPts[k] - p[1]) * (q[0] - p[0]) > 0:
                    valid = False
                    break

            # if the point is valid, add directed edge to the return list
            if valid:
                ret.append((p, q))

    return ret


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
    fileName = args.input

    numPoints, xs, ys = readPoints(fileName)

    solution = bruteForceHull(numPoints, xs, ys)

    if args.display:
        displayPoints(xs, ys, solution)
