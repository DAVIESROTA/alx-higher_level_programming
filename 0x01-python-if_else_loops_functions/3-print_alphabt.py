#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) == 'q' or chr(a) == 'e':
        continue
    print(chr(a).format(a), end='')
