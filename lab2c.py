#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Usage: ./lab2c.py <name> <age>")
    sys.exit(1)

name = sys.argv[1]
age = int(sys.argv[2])  # Convert age to an integer

print(f"Hi {name}, you are {age} years old.")

