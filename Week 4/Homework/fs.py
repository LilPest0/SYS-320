# File to traverse given directory & its subdirectories and retrieve all files
import argparse
import os
import searchLog

# Parser
parser = argparse.ArgumentParser(

    description="Traverses a directory and finds attacks or attempted attacks in web logs",
    epilog="Developed by Benji Gifford, Sept 26 2022"

)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse")
parser.add_argument("-s", "--searchterm", required="True", help="Traverses yaml file")

# Parse the arguments
args = parser.parse_args()
# Store root dir
rootdir = args.directory
# Store search term
searchterm = args.searchterm

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

# Look thru each log file
for eachfile in fList:

    check = searchLog.logs(eachfile,searchterm)

    # Create list of results
    results = []
    print(check)
    for eachfound in check:
        # Splits results
        attackcheck = eachfound.split(" ")
        results.append("\t URL: " + attackcheck[6] + " Status Code: " + attackcheck[8] + " File Size (Bytes): " + attackcheck[9])

    # Set results
    results = set(results)

    # Print results
    for eachvalue in results:
        print(eachvalue)




