import re, sys

def _syslog(filename,listOfKeywords):

    # Create an interface to search through syslog files
    # Open a file
    with open(filename) as f:
        
        # Read in file and save it to a variable
        contents = f.readlines()

    # lists to store results
    results = []

    # Loop throught the list returned, each element is a line from the smallSyslog
    for line in contents:

        #loops through keywords
        for eachKeyword in listOfKeywords:

            # if the line contains a keyword, it will be printed
            # searches and returns results using regular expression
            x = re.findall(r''+eachKeyword+'', line) 

            for found in x:

                #append the returned keywords to returns list
                results.append(found)

    # check to see if there are results
    if len(results) == 0:
        print("No results")
        sys.exit(1)

    # sort the list
    results = sorted(results)

    return results
    #print(x) 