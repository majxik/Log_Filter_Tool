import sys

arg_len=len(sys.argv)
#logcat_file=sys.argv[1]
#argument=sys.argv[2]
#keywords=sys.argv[3]

help = "Help:.\n" + \
           "-h prints out help containing info about all available switches.\n" + \
           "-s prints out the time difference between lines containing TEST STARTED and TEST FINISHED.\n" + \
           "-i <args,...> prints out lines containing all arguments.\n" + \
           "-e <args,...> print out all lines which don't contain any of provided arguments.\n" + \
           "Usage (Python): python logcat_parser.py logcat_file.txt -i word1,word2,word3"

if "-h" in sys.argv:
    print(help)
elif "-s" in sys.argv and arg_len == 3:
    print("argument -s")
    print([ line for line in open("logcat_file.txt") if "TEST STARTED" in line])
    print([ line for line in open("logcat_file.txt") if "TEST FINISHED" in line])
elif "-i" in sys.argv and arg_len == 4:
    keywords=sys.argv[3]
    keywords_list=keywords.split(",")
    for keyword in keywords_list:
        search_result=[line for line in open("logcat_file.txt") if keyword in line]
        print(keyword)
        for search_result_line in search_result:
            print(search_result_line)

elif "-e" in sys.argv and arg_len ==4:
    keywords=sys.argv[3]
    print("argument -e")
else:
    print("argument is invalid, check help for switches")

#print("logcat_file: ",logcat_file)
#print("argument: ",argument)
#print("keywords: ",keywords)
#input("press any key to continue")

#s = "11-30 04:39:49.878 === TEST FINISHED ==="
#match = re.search('\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}', s)
#date = datetime.datetime.strptime(match.group(), '%m-%d %H:%M:%S:%f')[:-3].date()
