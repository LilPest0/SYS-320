# File to traverse given directory & its subdirectories and retrieve all files
import argparse
import os
from xmlrpc.server import resolve_dotted_attribute

# Parser
parser = argparse.ArgumentParser(

    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Benji Gifford, Sept 21 2022"

)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse")

# Parse the arguments
args = parser.parse_args()

rootdir = args.directory

# Get information from cli
#print(sys.argv)

# Directory to traverse
# rootdir = sys.argv[1]

#print(rootdir)

# We will traverse a directory
# Check if argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()


# List to save files
fList = []

# Crawl thru givin directory with OS.Walk
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        #print(root + "/" + f)
        fileList = root + "\\" + f
        #print(fileList)
        fList.append(fileList)

#print(fList)

def statFile(toStat):

    # i is going to be the variable used for each of the metadata elements
    i = os.stat(toStat,follow_symlinks=False)

    # mode
    mode = i[0]

    # inode
    inode=i[1]

    # uid
    uid = i[4]

    # gid
    gid =i[5]

    # file size
    fsize = i[6]
    
    #access time
    atime = i[7]

    # modification time
    mtime = i[8]

    # ctime >> on windows is the birth of the file, when it was created
    # unix its when attributes of the file change
    ctime = i[9]
    crtime = i[9]
    
    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, mode, inode, uid, gid, fsize, atime, mtime, ctime, crtime))

for eachFile in fList:

    statFile(eachFile)
    


