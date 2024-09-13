import argparse


# main entry point for convex hull
if __name__ == '__main__':
    # take in arguments
    parser = argparse.ArgumentParser()

    # require an input file to read from
    parser.add_argument('input', help='Input file to read from', type=str)

    # todo: optional arguments here

    args = parser.parse_args()
    fileName = args.input

    # open and read points from file
    with open(fileName, 'r') as file:
        points = file.readlines()

    # remove newline characters
    points = [point.strip() for point in points]

    print(points)


