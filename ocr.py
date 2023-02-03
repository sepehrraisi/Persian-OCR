import sys, getopt
from OCR import detect

def main(argv):
   inputfile = ''
   mode = ''
   try:
      opts, args = getopt.getopt(argv,"hio:m:",["ifile=","ofile=","mode="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile> -m <mode>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile> -m <mode>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-i", "--ifile"):
         outputfile = arg
      elif opt in ("-o", "--ofile"):
         mode = arg
   detect.main(inputfile)
if __name__ == "__main__":
   main(sys.argv[1:])
