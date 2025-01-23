#!/usr/bin/env python3

# Author: Your Full Name
# Author ID: your_seneca_id
# Date Created: yyyy/mm/dd

import sys

# Check if an argument was provided
if len(sys.argv) > 1:
    try:
        timer = int(sys.argv[1])  # Convert first argument to integer
    except ValueError:
        print("Error: Please enter a valid integer.")
        sys.exit(1)
else:
    timer = 3  # Default timer value if no argument provided

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
