# Simple-iDRAC-Interface

A small command-line application written in Python to manage your Dell server. (Tested on Windows only)

![Image of SII in a Terminal](https://github.com/SomeCodecat/Simple-iDRAC-Interface/blob/main/sii.png)

Features include:
<br>- Monitoring system status
<br>- Starting a remote system
<br>- Stopping a remote system
<br>- Issuing custom commands

There are two Versions of the Software:
<br>[Default]
<br>- One is styled and and uses external packages that have to be installed with pip.
<br>[Nocolor]
<br>- The other one is kept simple and uses minimal external packages.

# Setup

Dependencies for both versions:
<br>Ipmitool should be installed and available in $PATH

Dependencies for the [Default] version:
<br>pip install termcolor
<br>pip install pyfiglet

<br>Open the downloaded Python script and set the Hostname [HOST] (iDRAC IP) to your desired value.

# Want to use both versions?

Start the [Nocolor] version with the -nocolor or -n flag when executing sii.bat.
