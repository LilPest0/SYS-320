import syslogCheck
import importlib
importlib.reload(syslogCheck)

# SSH authentication failures
def ssh_fail(filename, searchTerms):

    # call syslogcheck and return results
    is_found = syslogCheck._syslog(filename,searchTerms)

    # found list
    found = []

    # loop thru results
    for eachFound in is_found:

        #print(eachFound)
        #split results
        sp_results = eachFound.split(" ")

        #append split value to dound list
        found.append(sp_results[8]) 

    # Remove duplicates by using set, and convert list to dictionary
    hosts = set(found)

    # Print the results
    for eachHost in hosts:
        
        print(eachHost)
