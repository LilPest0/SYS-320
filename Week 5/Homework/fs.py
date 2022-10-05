# File to traverse given directory & its subdirectories and retrieve all files
import os, argparse, fsyaml

# Parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and finds attacks or attempted attacks in web logs",
    epilog="Developed by Benji Gifford, Oct 5 2022"
)

parser.add_argument("-d", "--directory", required=True, help="Directory containing CSV Files for analysis")
parser.add_argument("-p", "--program", required=True,help="Program to parse for (Registry, Script, PowerShell)")
parser.add_argument("-t","--terms",required=True,help="Term to search for")
parser.add_argument("-y","--yaml",required=True,help="Yaml configuration file")

# Parse the arguments
args = parser.parse_args()
# Store root dir
rootdir = args.directory
program = args.program 
terms = args.terms
yaml_file = args.yaml
# We will traverse a directory

# Check if argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))

# List to save files
fList = []

# Crawl thru givin directory with OS.Walk
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        #print(root + "/" + f)
        fileList = root + "/" + f
        #print(fileList)
        fList.append(fileList)
print("*"*60)
print("ATTACK DESCRIPTION")
if program == "Registry":
    print("The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services.\nSometimes these credentials are used for automatic logons. Adversaries could also inject malicious DLLs into registry keys that are loaded after reboot. When a user authenticates the DLLs have a routine that captures their credentials after login.")
if program == "Script":
    print("Adversaries may use scripts to aid in operations and perform multiple actions that would otherwise be manual. Scripting is useful for speeding up operational tasks and reducing the time required to gain access to critical resources.\nSome scripting languages may be used to bypass process monitoring mechanisms by directly interacting with the operating system at an API level instead of calling other programs. Common scripting languages for Windows include VBScript and PowerShell but could also be in the form of command-line batch scripts.")
if program == "PowerShell":
    print("PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.\nAdversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code.\nExamples include the Start-Process cmdlet which can be used to run an executable and the Invoke-Command cmdlet which runs a command locally or on a remote computer.")

print("*"*60)
print("Field Format: ARGUMENTS | HOSTNAME | PATH | PID | USERNAME")
print("*"*60)
for eachFile in fList:

    results = []
    found = fsyaml.logs(eachFile,program,terms,yaml_file)
    for eachFound in found:
        results.append(eachFound)

    if len(results) == 0:
        continue
    else:
        print("""File:{}""".format(eachFile))
        for eachValue in results:
            print(eachValue)
        print("*"*60)
