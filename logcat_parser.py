import sys
import datetime
from datetime import timedelta
from datetime import datetime

arg_len=len(sys.argv)
log_file=sys.argv[1]

help = "Help:.\n" + \
           "-h prints out help containing info about all available switches.\n" + \
           "-s prints out the time difference between lines containing 'TEST STARTED' and 'TEST FINISHED'.\n" + \
           "-i <args,...> prints out lines containing all arguments.\n" + \
           "-e <args,...> print out all lines which don't contain any of provided arguments.\n" + \
           "Usage (Python): python logcat_parser.py logcat_file.txt -i word1,word2,word3"
#Decision tree commanding script
if "-h" in sys.argv: #Print help, if arguments from command line contain -h switch
    print(help)
elif "-s" in sys.argv and arg_len == 3: #Print time diff between TEST STARTEd and TEST FINISHED lines
    test_started = [ line for line in open(log_file) if "TEST STARTED" in line]
    test_finished = [ line for line in open(log_file) if "TEST FINISHED" in line]

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
elif "-i" == sys.argv[2] and arg_len == 4: #Print only rows with arguments given in switch
    keywords=sys.argv[3]
    keywords_list=keywords.split(",")
    for line in open(log_file, 'r'):
        for expected in keywords_list:
            if expected in line:
                print(line)
elif "-e" == sys.argv[2] and arg_len ==4: #Print all rows except rows contains arguments given in switch
    keywords=sys.argv[3]
    keywords_list=keywords.split(",")
    for line in open(log_file, 'r'):
        exists = False
        for keyword in keywords_list:
            if keyword in line:
                exists = True
        if not exists:
            print(line)
else: #if non of option is valid, print error message.
    print("The argument is invalid, check the help for switches by the running script with -h switch(logcat_parser.py -h)")
