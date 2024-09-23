import argparse
import random

# main entry point for point generation
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # require an output file to write to
    parser.add_argument('output', help='Output file to write to', type=str)
    # require the number of points to generate
    parser.add_argument('numPoints', help='Number of points to generate', type=int)

    args = parser.parse_args()
    fileName = args.output
    numPoints = args.numPoints
    floor = -numPoints
    ceiling = numPoints

    numPtsGenerated = 0
    pts = []

    while numPtsGenerated < numPoints:
        x = random.randint(floor, ceiling)
        y = random.randint(floor, ceiling)

        # while not strictly necessary, this will prevent duplicate points
        if (x, y) not in pts:
            pts.append((x, y))
            numPtsGenerated += 1
        # pts.append((x, y))
        # numPtsGenerated += 1

    # open an output file to write to
    with open(fileName, 'w') as file:
        # write the number of points to the first line
        file.write(str(numPoints) + '\n')

        # write each point as two integers separated by a space on a new line
        for point in pts:
            file.write(str(point[0]) + ' ' + str(point[1]) + '\n')

    # close the file
    file.close()

    print('Points written to', fileName)
