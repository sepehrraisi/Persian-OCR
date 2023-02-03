import sys, getopt
from OCR import detect

def main(argv):
   inputfile = ''
   mode = ''
   try:
      opts, args = getopt.getopt(argv,"hi:m:",["ifile=","mode="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -m <mode>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -m <mode>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-m", "--mode"):
         mode = arg
   detect.main(inputfile)
if __name__ == "__main__":
   main(sys.argv[1:])
