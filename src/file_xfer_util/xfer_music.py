'''
Created on Mar 7, 2015

copyover_case2 
- copies files and directories from one directory to another such that 
  files with same name are not replaced, and if subdirectory A has [file 1, 2, 3] and
  sub directory B has [file 4, 5, 6], the result will be [file 1, 2, 3, 4, 5, 6] rather than
  replacing B with A -- > [file 4, 5, 6]
  
Useful for copying over music/other files to new computer

>> Readme on cases:

Every case (in it's original state) is in the Setup folder.
Copy both into the Tests folder to test a function


>>  USE THIS SCRIPT IN THE "Do What You Want" SECTION

@author: Alison Wong
'''

import os
import shutil #for copying/pasting

#directory of this script
pwd = os.path.abspath('')
print (pwd)





'''
Simple Case 1:  Folder 1 and Folder 2 only have files in them.
The goal is to copy over files in folder 1 that are not already in folder 2.
'''
def copyover_case1(source_path, dest_path):
    
    #list of folder 1 files
    sourcefileList = os.listdir(source_path)
    sourcefileList = [filename for filename in sourcefileList]
    
    destfileList = os.listdir(dest_path)
    destfileList = [filename for filename in destfileList]
    
    #for files in folder 1
    for f in sourcefileList:
        print("File: " + f)
       #check if there is a file with the same name in dest2.
        if (not os.path.isfile(dest_path + f)):
            shutil.copyfile(source_path + f, dest_path + f)
            print ("This file did not exist in dest2")
            
        print("")
        #if there is, never mind.  
        #Otherwise copy over

'''
>> Case 1 test:
result should be: 1 - 22 song tracks in case1dest
'''        
# case1source = pwd + '/Tests/case1start/'
# case1dest = pwd +'/Tests/case1dest/'
# print("Case 1")
# copyover_case1(case1source, case1dest)



'''
Simple Case 2:  Folder 1 and Folder 2 have 3rd level directories in them.
The goal is to copy over files in folder 1 that are not already in folder 2.

'''

def copyover_case2(source, dest):
    
    #source and dest
    source_path = source + "/"
    dest_path = dest + "/"
    
    print(" ")
    print ("copyover called!")
    print (source_path + " source path")
    print(dest_path + " dest path")
    #list of folder 1 files
    sourcefileList = os.listdir(source_path)
    sourcefileList = [filename for filename in sourcefileList]
    
    destfileList = os.listdir(dest_path)
    destfileList = [filename for filename in destfileList]
    
    #for files in folder 1
    for f in sourcefileList:
        print("File: " + f)
        
        #check if there is a file with the same name in dest2.
        if (not (os.path.isfile(dest_path + f))):
            
            #if directory
            if (os.path.isdir(dest_path + f)): #do the same for the files within the idrectory
                print("It's a directory!")
                print("source path is " + dest_path + f)
                print("dest path is " + dest_path)
                copyover_case2(source_path + f, dest_path + f)
                
                #problem: it is a directory, but it is not going there.
                            
            #otherwise, copy
            else:
                shutil.copyfile(source_path + f, dest_path + f)
                print ("Love darling")
            
            
        print("")
        #if there is, never mind.  
        #Otherwise copy over
    return 1

'''
>> Case 2 Test
result should be: 1-22 in every directory of case2dest
'''
# case2source = pwd + '/Tests/case2start'
# case2dest = pwd + '/Tests/case2dest'
 
# print(" ")
# print("Case 2")
# copyover_case2(case2source, case2dest)



'''
Simple Case 3: Case 2 with non-standard (Japanese or Chinese) names and symbols such as * ~ / 
and also with several directories

>> Case 3 Test
result should be: 1 - 5 in every directory of case3dest
'''
# case3source = pwd + '/Tests/case3start'
# case3dest = pwd + '/Tests/case3dest'

# copyover_case2(case3source, case3dest)










'''
Do What You Want Section
'''


#copy music (not done)
#my hard drive
# source = ''
# dest = '~/Music/iTunes/iTunes Media/Music'

# copyover_case1(source, dest)













   