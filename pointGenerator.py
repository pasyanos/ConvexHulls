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
    floor = -numPoints//2
    ceiling = numPoints//2

    # open an output file to write to
    with open(fileName, 'w') as file:
        # write the number of points to the first line
        file.write(str(numPoints) + '\n')

        # write the points to the file
        for i in range(numPoints):
            x = random.randint(floor, ceiling)
            y = random.randint(floor, ceiling)
            file.write(str(x) + ' ' + str(y) + '\n')

    # close the file
    file.close()

    print('Points written to', fileName)
