# Python-RE-XED

I wrote a Python wrapper for my Reverse Engineering Assignment that let me analyze PE files by launching Intel's x86 Encoder/Decoder.  This takes an executable and then decodes the instructions and converts them into their assembly representation from the binary instructions. This also provides a hex dump and all of the operations that the processor is given in assembly.

Inside is a report, the program, and the disassembling tool I used to make all of it.

It's a pretty neat thing that helps you understand assembly and processor architecture.

Introduction
Assignment five built largely off of the work that was done in assignment four. Assignment four
gave us XED, a robust decoder and encoder tool that allows us to do deep analysis of binary
files. To extend on this assignment, I’ve decided to build a graphical user interface to accompany
the usage of XED, as well as implement a search feature that allows you to find particular
registers or HEX strings within the assembly dump file.
I originally meant to provide support for both the .text and .data sections, but in the
current implementation, the only thing that is supported is the text section. In place of the data
section is the console output from XED’s statistical analysis. This left the number of tools
utilized to be fairly few ­ instead of using a wrapper, we simply used XED and wrote our own
wrapper within a program.
Disassembler Features:
­ Decodes any PE file.
­ Provides console output for the decoding process.
­ Provides statistical information regarding the decoding process, including, but not limited
to, number of instructions decoded, number of decode errors, and the number of invalid
instructions.
­ Built­in wrapper for XED from a Python­based script.
­ Search feature implemented that allows you to search for a decoded instruction or HEX
string and it will highlight all occurrences within the file.
Disassembler Requirements:
­ Python 2.7 (not Python 3)
­ XED (the EXE available from Intel)
­ PE file for testing
­ Permissions to create text files.
Usage of this disassembler is extremely straight­forward and simple. The Python script
handles most of the work for you, so you simply have to navigate to the directory containing the
Python script and XED and execute it. It’s imperative that the XED executable be in the same
directory as the Python script.
