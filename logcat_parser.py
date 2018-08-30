import sys
#print("number of arguments:", len(sys.argv), "arguments")
#print("argument list", str(sys.argv))

arg_len=len(sys.argv)
logcat_file=sys.argv[1]
argument=sys.argv[2]
keywords=sys.argv[3]

help = "Help:.\n" + \
           "-h prints out help containing info about all available switches.\n" + \
           "-s prints out the time difference between lines containing TEST STARTED and TEST FINISHED.\n" + \
           "-i <args,...> prints out lines containing all arguments.\n" + \
           "-e <args,...> print out all lines which don't contain any of provided arguments.\n" + \
           "Usage (Python): python logcat_parser.py logcat_file.txt -i word1,word2,word3"

if argument == "-h":
    print(help)
elif argument == "-s":
    print("argument -s")
elif argument == "-i":
    print("argument -i")
elif argument == "-e":
    print("argument -e")
else:
    print("argument ",argument," is invalid")

#print("logcat_file: ",logcat_file)
#print("argument: ",argument)
#print("keywords: ",keywords)
input("press any key to continue")
