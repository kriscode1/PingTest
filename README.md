# PingTest
Tracks remote disconnections by parsing and recording output from Microsoft's ping utility.

## Usage

Call pingtest(target_name, ping_count) to run the command "ping target_name -n ping_count". Then pingtest() will return a list of times for each ping_count pings. 

* time == -1 is error
* time == 0 is when ping <1ms
* time >= 1 is the time in milliseconds

This was written to test various servers for network connectivity, continously, and discover if any disconnections occured while away. The times were logged with a little formatting to a TSV file to be sorted and check for any -1 time values (disconnections). An example of this is in pingtest.py. Example output below, pinging each target twice:

    2017-10-12 19:39:00.817122      192.168.0.1     2       2
    2017-10-12 19:39:01.849578      google.com      14      14
    2017-10-12 19:39:02.910976      10.60.17.103    -1      -1
    2017-10-12 19:39:11.848790      209.88.198.133  153     160
    2017-10-12 19:39:13.035685      192.168.0.1     1       1
    2017-10-12 19:39:14.067242      google.com      14      12
    2017-10-12 19:39:15.108837      10.60.17.103    -1      -1
    2017-10-12 19:39:23.848390      209.88.198.133  150     148
    2017-10-12 19:39:25.010907      192.168.0.1     1       1
    2017-10-12 19:39:26.035119      google.com      13      16
