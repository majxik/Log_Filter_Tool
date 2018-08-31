import sys
import datetime
from datetime import timedelta
from datetime import datetime

arg_len=len(sys.argv)

help = "Help:.\n" + \
           "-h prints out help containing info about all available switches.\n" + \
           "-s prints out the time difference between lines containing 'TEST STARTED' and 'TEST FINISHED'.\n" + \
           "-i <args,...> prints out lines containing all arguments.\n" + \
           "-e <args,...> print out all lines which don't contain any of provided arguments.\n" + \
           "Usage (Python): python logcat_parser.py logcat_file.txt -i word1,word2,word3"
#Decision tree comanding script
#Print help, if arguments from comand line contain -h switch
if "-h" in sys.argv:
    print(help)
elif "-s" in sys.argv and arg_len == 3:
    test_started = [ line for line in open("logcat_file.txt") if "TEST STARTED" in line]
    test_finished = [ line for line in open("logcat_file.txt") if "TEST FINISHED" in line]

    start_time_parsed=datetime.strptime(test_started[0].split(" ===")[0], "%m-%d %H:%M:%S.%f")
    end_time_parsed=datetime.strptime(test_finished[0].split(" ===")[0], "%m-%d %H:%M:%S.%f")

    timedelta=end_time_parsed-start_time_parsed
    timedelta_in_sec=timedelta.total_seconds()
    years=divmod(timedelta_in_sec, 31556926)[0]
    days=divmod(timedelta_in_sec, 86400)[0]
    hours = divmod(timedelta_in_sec, 3600)[0]
    minutes = divmod(timedelta_in_sec, 60)[0]
    seconds = timedelta_in_sec
    microseconds = timedelta.microseconds

    print("Test took: ",years,"years",days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")
#Filter in, number of arguments must be at least 4 (python_script.py textfile.txt switcher word1,word2,word3)
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
    keywords_list=keywords.split(",")
    for keyword in keywords_list:
        search_result=[line for line in open("logcat_file.txt") if keyword not in line]
        print(keyword)
        for search_result_line in search_result:
            print(search_result_line)

    print("argument -e")
else:
    print("argument is invalid, check help for switches by running script with -h switch(logcat_parser.py -h)")

#python logcat_parser.py -i logcat_file.txt I/InstallerConnection,I/Vold

#print("logcat_file: ",logcat_file)
#print("argument: ",argument)
#print("keywords: ",keywords)
#input("press any key to continue")

#s = "11-30 04:39:49.878 === TEST FINISHED ==="
#match = re.search('\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}', s)
#date = datetime.datetime.strptime(match.group(), '%m-%d %H:%M:%S:%f')[:-3].date()
