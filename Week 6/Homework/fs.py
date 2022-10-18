import os, sys, argparse, paramiko, yaml
from getpass import getpass

# parser
parser = argparse.ArgumentParser(

    description= "Traverses a directory and builds a forensic body file",
    epilog= "Developed by Benjamin Walter Gifford III, 20221017"
)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

# Parse the arguments
args = parser.parse_args()
# Stores root directory
rootdir = args.directory

if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        #print(root  + "/" + f)
        fileList = root  + "/" + f
        #print(fileList)
        fList.append(fileList)

with open('searchTerms.yaml', 'r') as yf:
    keywords = yaml.safe_load_all(yf)
    
    # loops through key words, prints attack desription
    for keyVal in keywords:
        for key, value in keyVal.items():
            cmds = value['cmd']
            commands = cmds.split(",")
            print(commands)


def statFile(toStat):
    i = os.stat(toStat==False)

    mode = i[0] 
    
    inode=i[1]

    uid = i[4]

    gid = i[5]

    # filesize
    fsize = i[6]

    # access  time
    atime = i[7]

    # modification time
    mtime = i[8]

    # ctime => windows is the birth of the file, when it was created
    # unix it is when attributes of the file changes
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))

for eachFile in fList:
    statFile(eachFile)

