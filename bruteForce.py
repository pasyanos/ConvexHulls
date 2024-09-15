import argparse
from utils import readPoints
from utils import displayPoints


# main entry point for convex hull
if __name__ == '__main__':
    # take in arguments
    parser = argparse.ArgumentParser()

    # require an input file to read from
    parser.add_argument('input', help='Input file to read from', type=str)

    args = parser.parse_args()
    fileName = args.input

    xs, ys = readPoints(fileName)
    displayPoints(xs, ys)
