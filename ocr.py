import getopt
import sys
from OCR import detect


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "h:i", ["ifile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    detect.main(inputfile)
if __name__ == "__main__":
    main(sys.argv[1:])
