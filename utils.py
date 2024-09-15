import matplotlib
import matplotlib.pyplot


# open a file and read in points from it
def readPoints(fileName):
    # open the file
    with open(fileName, 'r') as file:
        points = file.readlines()

    xs, ys = {}, {}

    # the first line is the number of points,  so remove it
    points = points[1:]

    # each remaining line is a point with integer x and y coordinates
    points = [point.strip().split() for point in points]
    # read x coords into xs list and y coords into ys list
    xs = [int(point[0]) for point in points]
    ys = [int(point[1]) for point in points]

    # print(xs, ys)
    return xs, ys


# display given points in a scatter plot
def displayPoints(xs, ys):
    matplotlib.pyplot.scatter(xs, ys)
    matplotlib.pyplot.show()
