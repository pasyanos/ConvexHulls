import matplotlib
import matplotlib.pyplot


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
def displayPoints(xs, ys, solution=None):
    matplotlib.pyplot.scatter(xs, ys)

    if solution:
        for edge in solution:
            matplotlib.pyplot.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], 'r-')

    matplotlib.pyplot.show()


# write the solution to an output text file
# it is up to the algorithm calling this function to ensure the points are in
# the correct counterclockwise order.
def writeSolution(outFile, numPts, solutionPoints):
    # open the file to write to
    with open(outFile, 'w') as file:
        # write the number of points
        file.write(str(numPts) + '\n')

        # write each point
        for point in solutionPoints:
            file.write(str(point[0]) + ' ' + str(point[1]) + '\n')

    # close the file
    outFile.close()
