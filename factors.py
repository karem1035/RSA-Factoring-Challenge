#!/usr/bin/env python3

import sys

file =  open(sys.argv[1], "r")
for i in file:
    i = int(i)
    prime = 2
    while True:
        if i % prime != 0:
            prime +=1
            continue
        break
    print(f"{i}={int(i / prime)}*{prime}")
        