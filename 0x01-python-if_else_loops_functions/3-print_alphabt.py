#!/usr/bin/python3
for letter in range(97, 123):
if chr(letter) is not '101' and chr(letter) is not '113':
continue
print(chr(letter).format(), end="")
