import matplotlib
import matplotlib.pyplot
import numpy as np


# given 3 points, calculate the determinant of the matrix formed by them
def calculateTurnDeterminant(p, q, r):
    # matrix from three points
    mat = np.array([[1, p[0], p[1]],
                    [1, q[0], q[1]],
                    [1, r[0], r[1]]])

    # determinant of the matrix
    return np.linalg.det(mat)


# open a file and read in points from it
def readPoints(fileName):
    # open the file
    with open(fileName, 'r') as file:
        points = file.readlines()

    # the first line is the number of points
    numPoints = int(points[0].strip())
    points = points[1:]

    # each remaining line is a point with integer x and y coordinates
    points = [point.strip().split() for point in points]
    # read x coords into xs list and y coords into ys list
    xs = [int(point[0]) for point in points]
    ys = [int(point[1]) for point in points]

    # print(numPoints, xs, ys)
    return numPoints, xs, ys


# display given points in a scatter plot
def displayPoints(n, xs, ys, solutionPoints, solutionEdges, method):
    matplotlib.pyplot.scatter(xs, ys)

    # draw solution edges in red
    for edge in solutionEdges:
        p, q = edge
        matplotlib.pyplot.plot([p[0], q[0]], [p[1], q[1]], color='r')

    # draw solution points in red over lines, and label the order
    index = 1
    for point in solutionPoints:
        matplotlib.pyplot.scatter(point[0], point[1], color='r')
        matplotlib.pyplot.text(point[0], point[1], str(index))
        index += 1

    # set the title of the plot
    matplotlib.pyplot.title(str(n) + " Point " + method + " Convex Hull")

    matplotlib.pyplot.show()


# write the solution to an output text file
# it is up to the algorithm calling this function to ensure the points are in
# the correct counterclockwise order.
def writeSolution(outFile, solutionPoints):
    # open the file to write to
    with open(outFile, 'w') as file:
        # write the number of points
        numPts = len(solutionPoints)
        file.write(str(numPts) + '\n')

        # write each point as two integers separated by a space on a new line
        for point in solutionPoints:
            file.write(str(point[0]) + ' ' + str(point[1]) + '\n')

    # close the file
    file.close()


# given a start and end time, calculate runtime
def calculateRuntime(start, end):
    return end - start
