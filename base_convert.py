#! /usr/bin/env python3

"""
Leif Gregory <leif@devtek.org>
Base Encoder Tutorial
Tested to Python v3.10.7

Changelog
20230314 -  Initial Code

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import base64
import sys

def convert(conv_type, str_to_conv):
    
    # Convert input(s) into decimal as a starting place for all encodings
    if conv_type == 'bin':
        decimal = int(str_to_conv, 2)
    elif conv_type == 'bcd':
        decimal = int(str_to_conv)
    elif conv_type == 'chr':
        decimal = ord(str_to_conv)
    elif conv_type == 'dec':
        decimal = int(str_to_conv)
    elif conv_type == 'hex':
        decimal = int(str_to_conv, 16)
    elif conv_type == 'oct':
        decimal = int(str_to_conv, 8)
    
    # Set up dict to track all conversions
    encodings = {"decimal": decimal}

    # Convert to binary and inverse
    encodings["binary"] = format(encodings["decimal"], '08b')
    encodings["binary_inv"] = ''.join('1' if x == '0' else '0' for x in encodings["binary"])

    # Convert to decimal inverse
    encodings["decimal_inv"] = int(encodings["binary_inv"], 2)

    # Convert to hexadecimal and inverse
    encodings["hex"] = format(encodings["decimal"],'02x').upper()
    encodings["hex_inv"] = format(encodings["decimal_inv"],'02x').upper()

    # Convert to octal and inverse
    encodings["octal"] = format(encodings["decimal"],'03o').upper()
    encodings["octal_inv"] = format(encodings["decimal_inv"],'03o').upper()

    # Convert to ASCII char and inverse and replace unprintable chars
    if (encodings["decimal"] in range(33, 127) or encodings["decimal"] in range(161,256)) and encodings["decimal"] != 173:
        encodings["char"] = chr(encodings["decimal"])
    else:
        encodings["char"] = 'xxx'

    # Convert to BCD
    encodings["bcd"] = " ".join(format(int(x), '04b') for x in str(encodings["decimal"]))
    encodings["bcd_inv"] = " ".join(format(int(x), '04b') for x in str(encodings["decimal_inv"]))

    # Base16 conversion of input
    encodings["b16"] = base64.b16encode(str_to_conv.encode('utf-8')).decode('utf-8')

    # Base32 conversion of input
    encodings["b32"] = base64.b32encode(str_to_conv.encode('utf-8')).decode('utf-8')

    # Base64 conversion of input
    encodings["b64"] = base64.b64encode(str_to_conv.encode('utf-8')).decode('utf-8')

    # Base85 conversion of input
    encodings["b85"] = base64.a85encode(str_to_conv.encode('utf-8')).decode('utf-8')
    
    return encodings


encodings = convert(sys.argv[1], sys.argv[2])

for k, v in encodings.items():
    print(f'{k.upper()}: {v}')
