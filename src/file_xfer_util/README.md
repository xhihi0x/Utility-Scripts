file_xfer_util

This utility is useful for transferring music from a backup to the itunes/media/music folder on a new computer.

From the old directory to the new directory, copies over files that do not exist in the new directory but do in the old directory
to the new directory without replacing the files in the new directory.  
(Useful because if one copies over the music folder normally, the old subdirectories will simply replace the new ones).  It does
not copy over duplicate files in the new directory.

For example:
S'pose we have dir1 and dir2, and we are copying from dir1 to dir 2

dir1 has:
1/bla.txt, bla2.txt, bla3.txt
2/bla4.txt, bla5.txt

dir2 has:
1/bla.txt, bla6.txt, bla5.txt
2/bla4.txt, bla7.txt

dir2/1/bla.txt will not be replaced with dir1/1/bla.txt, and so on..
The end result will be:

dir2 has:
1/bla.txt, bla2.txt, bla3.txt, bla5.txt, bla6.txt
2/bla4.txt, bla5.txt, bla7.txt

**************************************************************************
To use this script (Under "Do what you want section" at the bottom):
**************************************************************************

source = 'put the address of dir1 you want to copy from here'
dest = 'put the address of dir2 here'

copyover_case2(source, dest)
