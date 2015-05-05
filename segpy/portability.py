import os
import sys

EMPTY_BYTE_STRING = b'' if sys.version_info >= (3, 0) else ''


if sys.version_info >= (3, 0):
    izip = zip
    from itertools import zip_longest as izip_longest
else:
    from itertools import (izip, izip_longest)
    izip = izip                  # Keep the static analyzer happy
    izip_longest = izip_longest  # Keep the static analyzer happy


if sys.version_info >= (3, 0):
    def four_bytes(byte_str):
        a, b, c, d = byte_str[:4]
        return a, b, c, d
else:
    def four_bytes(byte_str):
        a = ord(byte_str[0])
        b = ord(byte_str[1])
        c = ord(byte_str[2])
        d = ord(byte_str[3])
        return a, b, c, d

if sys.version_info >= (3, 0):
    unicode = str
else:
    unicode = unicode




