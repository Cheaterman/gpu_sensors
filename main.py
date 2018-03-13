#!/usr/bin/env python

import os
import subprocess
import time


def main():
    gpu_temps = [
        int(temp) for temp in subprocess.check_output(
            'primusrun nvidia-settings -c :8 -q gpucoretemp -t'.split(' ')
        ).split()
    ]
    average_temp = sum(gpu_temps) / float(len(gpu_temps))
    with open(
        os.path.join(os.path.dirname(__file__), 'temperature'), 'w'
    ) as temp_file:
        temp_file.write('temperature: %d00\n' % average_temp)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
