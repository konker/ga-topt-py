ga-topt-py
------------------------------------------------------------------------------

A command line tool to generate Google Authenticator tokens widely used for multi-factor authentication.

Requires the shared secret to be made available in one of the following ways:
- Through stdin
- By specifiying a file which contains the secret as an argument

Prints the current code to stdout.

Basically a direct translation of the [Wikipedia pseudo-code](https://en.wikipedia.org/wiki/Google_Authenticator#Pseudocode_for_Event.2FCounter_OTP) into Python3


## Example usage
    $ ./ga-topt-py my-secret.txt
    413401

