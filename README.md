ga-topt-py
------------------------------------------------------------------------------

Quick way to generate Google Authenticator tokens widely used for multi-factor authentication

Requires the shared secret to be made available:
- through stdin
- or by specifiying a file which contains the secret as an argument

Prints the current code to stdout.

Basically a direct translation of the Wikipedia pseudo-code into Python3

[https://en.wikipedia.org/wiki/Google_Authenticator#Pseudocode_for_Event.2FCounter_OTP](https://en.wikipedia.org/wiki/Google_Authenticator#Pseudocode_for_Event.2FCounter_OTP)

## Example usage
    $ ./ga-topt-py my-secret.txt
    41340

