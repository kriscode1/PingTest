'''Contains pingtest(), to run Microsoft's ping utility and parse output.
Tracks remote disconnections by parsing and recording output from Microsoft's ping utility.

Kristofer Christakos 2017
'''

import subprocess    #For running Microsoft's ping utility in pingtest()
import datetime        #For outputting time in log file, not needed in pingtest()
import sys             #For the tests only, not needed in pingtest()

def pingtest(target_name, ping_count):
    '''Runs "ping target_name -n ping_count" and parses output as list of times.
    Time -1 is error, 0 is when ping <1ms, and time >=1 is in milliseconds
    '''
    process = subprocess.run("ping " + target_name + " -n " + str(ping_count), stdout=subprocess.PIPE)
    result = process.stdout.decode("utf-8").splitlines()
    times = []
    for line in result[2: 2 + ping_count]:
        time_index = line.find("time")
        if (time_index == -1): 
            times.append(-1)    #Request timed out.
            continue
        time_index += 4
        space_index = line.find(" ", time_index)
        if (space_index == -1):
            times.append(-1)    #Error
            continue
        if (line[time_index] == '='): time_index += 1
        time_str = line[time_index:space_index]
        if (time_str == "<1ms"): times.append(0)
        else:
            time = time_str[0:-2]
            try:
                times.append(int(time))
            except:
                times.append(-1)
    return times

def get_timestamp():
    return str(datetime.datetime.now())

def join_ints(int_list, separator):
    '''Inputs list of ints and joins them to a string.
       Example input:    [1, 2, 3, 4], '\t'
       Example output:   "1\t2\t3\t4"
    '''
    return separator.join([str(n) for n in int_list])

def pingtest_and_write(server, file_handle=None, yes_print=True):
    '''Perform pingtest, then do custom formatting and write to log and print.'''
    timestamp = get_timestamp()
    times = pingtest(server, 2)
    writestr = timestamp + '\t' + server + '\t' + join_ints(times, '\t') + '\n'
    if yes_print: print(writestr, end='')
    if (file_handle != None): file_handle.write(writestr)


### Run some tests using the above functions ###

f = None
if (len(sys.argv) == 2):
    try:
        f = open(sys.argv[1], "a")
    except:
        print("Could not open file to log to.");
        sys.exit()
else:
    print("Enter a single parameter to store log file. Currently not logging.")

while(True):
    pingtest_and_write("192.168.0.1", f)
    pingtest_and_write("google.com", f)
    pingtest_and_write("10.60.17.103", f)
    pingtest_and_write("209.88.198.133", f) #GreenTeamDNS 2
    f.flush()
