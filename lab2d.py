#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Ensure that we exit with a status code of 0

name = sys.argv[1]
age = sys.argv[2]  # Assuming age is entered as a string

print(f"Hi {name}, you are {age} years old.")
