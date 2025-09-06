Dependencies you need:
time (installed standard as part of python)
pwninput 
pyfiglet

Features:
Input a number, the program then "thinks" what your number is and prints it, no actual mind reading just a display of the time function and a working progress bar.
note: though the progress bar code appears to be copied from stack overflow, I did take my time to understand how it works so this isn't just a remix of other people's work.

Funny things to note: Version 1.0 and 1.0-VSC take significantly longer to load because I made funny number bigger, this can be edited very simply by changing
the following code: 
items = list(range(0, 500))
to:
items = list(range(0, 5))
or whatever number you desire.

Enjoy getting your mind read!

