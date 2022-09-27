import re, sys, yaml
import searchLog

# search thru logs
def logs (logfile,searchterm):
# Open the Yaml file 
        try:
            with open('searchTerms.yaml', 'r') as yf:
                keywords = yaml.safe_load_all(yf)
                terms = searchterm

                # Make list of keywords to scan
                listOfKeywords = terms.split(", ")

                # Open a file
                with open(logfile) as f:
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

        except EnvironmentError as e:
            print(e.strerror)


