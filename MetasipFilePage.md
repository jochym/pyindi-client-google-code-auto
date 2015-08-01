# The metasip file #

## Presentation ##

The Python binding of the libindi library has been made with the [metasip](http://www.riverbankcomputing.com/hg/metasip/) package. This package is the one used for the PyQt binding itself. The principle of operation is to scan some given directories and select some include files, then to parse each selected include file to retain classes, types and methods we would like to bind. The tool generates the corresponding sip files. The point is mainly to add wrapper code for types that sip is unable to automatically bind itself.


## Installation/Use of metasip ##

use `msip pyindi.msp` to edit/create the metasip file. pyindi is the name of the metasip project, PyIndi the name of the python module.

In module properties, set the default encoding to ASCII (str in both Python 2 and 3).

First, set source directory in the scanner to the latest version of libindi source files, file filter to `*`.h, and parser arguments to -I/usr/include/libindi and create a new header directory:
  1. for libindi/libs (IndiApi): ignore all but indiapi.h and indidevapi.h
  1. for libindi/libs/indibase: ignore al but baseclient.h, basedevice.h, indibase.h and indiproperty.h

To generate the sip files in a sip directory, use `mkdir sip; msip -g sip pyindi.msp`


## Sip Configuration ##
The file pyindi-configure.py contains all the stuff to configure, generate and install the binding module.

## The client binding ##

### indidevapi.h ###