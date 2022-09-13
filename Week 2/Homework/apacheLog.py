import logCheck
import re
import importlib
importlib.reload(logCheck)

# Apache events
def bytes(filename, service, term):

    # call syslogcheck and return results
    is_found = logCheck._logs(filename, service, term)

    # found list
    found = []

    # loop thru results
    for eachFound in is_found:

        # print(eachFound)
        # split results
        sp_results = eachFound.split(" ")
        
        for item in sp_results:
            if bool(re.search(r"qq", item)):
                sp_results.remove(item)
        # append split value to found list
        # "GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"

        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4]+ " bytes sent " + sp_results[7] + " bytes received ") 

    # Remove duplicates by using set, 
    # and convert list to dictionary
    getValue = set(found)

    # Print the results
    for eachValue in getValue:
        
        print(eachValue)


# Looks through logs and finds all "QQ" files where there is a proxy opened message
def proxy(filename, service, term):

    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, service, term)

    # found list
    found = []

    # Loop thru results
    for eachFound in is_found:

        # print(eachFound) & split results
        sp_results = eachFound.split(" ")

        # For loop in sp_results that filters out lowercase qq
        for item in sp_results:
            if bool(re.search(r"qq", item)):
                sp_results.remove(item)

        # Append the split value to the found list
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " through proxy") #Through replaces 4 and 5

    # Convert list to dictionary
    getValue = set(found)

    # Print results
    for eachValue in getValue:

        print(eachValue)

