#!/usr/bin/env python3

# Author: Your Full Name
# Author ID: your_seneca_id
# Date Created: yyyy/mm/dd

import sys

# Convert the first command line argument to an integer for the countdown
timer = int(sys.argv[1])  # Make sure to handle IndexError and ValueError if needed

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
