#!/usr/bin/python

import sys
import datetime
import os

args = sys.argv
import shutil
shutil.copyfile(args[1], 'temp_file')
result = open(args[1], 'w')

def increment(one):
    time = one.split(',')[0]
    seconds = int(time.split(':')[2])
    minutes = int(time.split(':')[1])
    hours = int(time.split(':')[0])
    temp_time = datetime.datetime(1, 1, 1, hours, minutes, seconds)
    try:
        temp_time = temp_time + datetime.timedelta(seconds=int(args[2]))
    except:
        # print('time cannot be negative!')
        pass
    time = temp_time.time()
    time = str(time) + ',' + one.split(',')[1]
    return time

def correct():
    try:
        f = open('temp_file')
    except:
        print('Check file name.')

    lines = f.readlines()

    for line in lines:
        arrow = '-->'
        if arrow in line:
            temp = line.split(arrow)
            one = temp[0]
            two = temp[1].strip()
            one = increment(one)
            two = increment(two)
            res = one + '--> ' + two + '\n'
            result.write(res)

        else:
            result.write(line)

    f.close()
    result.close()
    os.remove('temp_file')

if __name__ == '__main__':
    correct()




