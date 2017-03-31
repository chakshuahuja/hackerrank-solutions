# https://www.hackerrank.com/challenges/time-conversion
import sys

time = raw_input().strip()
tformat = time[-2:]
hours = time[:2]
if tformat == 'AM':
    if hours == '12':
        print '0' + str(int(time[:2])-12) + time[2:-2]
    else:
        print time[:-2]
else:
    if hours == '12':
        print time[:-2]
    else:
        print str(int(time[:2])+12) + time[2:-2]