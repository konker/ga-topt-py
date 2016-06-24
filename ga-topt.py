#!/usr/bin/env python3

# ga-topt.py
#
# Author: Konrad Markus <konker@luxvelocitas.com>
#
# Quick way to generate Google Authenticator tokens widely used for multi-factor authentication
# Requires the shared secret to be made available:
# either through stdin or by specifiying a file which contains the secret as an argument
# Prints the current code to stdout
#
# Basically a direct translation of the Wikipedia pseudo-code into Python3
#
#  From wikipedia:
#  https://en.wikipedia.org/wiki/Google_Authenticator#Pseudocode_for_Event.2FCounter_OTP
#
#  function GoogleAuthenticatorCode(string secret)
#      key := base32decode(secret)
#      message := floor(current Unix time / 30)
#      hash := HMAC-SHA1(key, message)
#      offset := last nibble of hash
#      truncatedHash := hash[offset..offset+3]  //4 bytes starting at the offset
#      Set the first bit of truncatedHash to zero  //remove the most significant bit
#      code := truncatedHash mod 1000000
#      pad code with 0 until length of code is 6
#      return code
#

import sys
import time
import math
import fileinput
import hashlib
import hmac
import base64


def main():
    # Read the file if given as an argument, or read from stdin
    for line in fileinput.input():
        secret = line.strip()
        break

    # key := base32decode(secret)
    key = base64.b32decode(secret)

    # message := floor(current Unix time / 30)
    message = math.floor(time.time() / 30).to_bytes(8, 'big')

    # hash := HMAC-SHA1(key, message)
    hash = bytearray(hmac.new(key, message, hashlib.sha1).digest())

    # offset := last nibble of hash
    offset = int.from_bytes([hash[-1]], 'big') & 0x0F

    # truncatedHash := hash[offset..offset+3]  //4 bytes starting at the offset
    truncated_hash = hash[offset:offset+4]

    # Set the first bit of truncatedHash to zero  //remove the most significant bit
    truncated_hash[0] = (int.from_bytes([truncated_hash[0]], 'big') & 0x7F)

    # code := truncatedHash mod 1000000
    code = int.from_bytes(truncated_hash, 'big') % 1000000

    # pad code with 0 until length of code is 6
    print('{0:06d}'.format(code))


if __name__ == '__main__':
    main()

