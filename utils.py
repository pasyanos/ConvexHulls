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
